from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
import time
import testTree

NUM_ITERATION = 5

def training(sc, inputFile, numPartitions):
  print("Test with file " + inputFile + " with " + str(numPartitions) + " partition(s)")
  stats = []
  
  rawRDD = sc.textFile(inputFile, numPartitions)
  labeledRDD = rawRDD.map(lambda line: line.split(','))\
    .map(lambda row: LabeledPoint(row[-1], row[0:-1]))
    
  trainingRDD, testRDD = labeledRDD.randomSplit([0.7, 0.3])
  
  #Training of the model !
  timeBegin = time.time()
  for i in range(0, NUM_ITERATION):
    model = testTree.trainModel(sc, trainingRDD)
  timeEnd = time.time()
  
  totalTime = timeEnd - timeBegin
  meanTime = totalTime/NUM_ITERATION

  stats.append(meanTime)
  
  print("Total time of training : " + str(totalTime))
  print("Mean time of training : " + str(meanTime))

  #Evaluating the model
  predictions = model.predict(testRDD.map(lambda test: test.features))
  labelAndPrediction = testRDD.map(lambda test: test.label).zip(predictions)

  errorCount = labelAndPrediction.filter(lambda lp: lp[0] != lp[1]).count()
  accuracy = float(errorCount)/float(testRDD.count())

  stats.append(accuracy)
  
  print("Total number of error : " + str(errorCount))
  print("Error proportion : " + str(accuracy))

  return stats
