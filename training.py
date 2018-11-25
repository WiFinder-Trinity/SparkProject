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
  model_num = trainingRDD.count()
  test_num = testRDD.count()
  
  #Training of the model !
  timeBegin = time.time()
  for i in range(0, NUM_ITERATION):
    model = testTree.trainModel(sc, trainingRDD)
  timeEnd = time.time()
  
  totalTime = timeEnd - timeBegin
  meanTime = totalTime/NUM_ITERATION

  stats += [model_num, test_num, meanTime]
  
  print("Total time of training : " + str(totalTime))
  print("Mean time of training : " + str(meanTime))

  #Evaluating the model
  timeBegin = time.time()
  predictions = model.predict(testRDD.map(lambda test: test.features))
  timeEnd = time.time()
  labelAndPrediction = testRDD.map(lambda test: test.label).zip(predictions)

  errorCount = labelAndPrediction.filter(lambda lp: lp[0] != lp[1]).count()
  prediction_time = timeEnd - timeBegin
  mean_prediction_time = prediction_time/float(test_num)
  accuracy = float(errorCount)/float(test_num)

  stats = stats + [mean_prediction_time, accuracy] 
  
  print("Prediction time : " + str(prediction_time))
  print("Mean prediction time : " + str(mean_prediction_time))
  print("Total number of error : " + str(errorCount))
  print("Error proportion : " + str(accuracy))

  return stats
