import testTree

NUM_ITERATION = 5

def training(sc, inputFile, numPartitions):
  print("Test with file " + dataFile + "with " + numPartitions " partition(s)")
  rawRDD = sc.textFile(inputFile, numPartitions)
  labeledRDD = rawRDD.map(lambda line: line.split(','))\
    .map(lambda row: LabeledPoint(row[-1], row[0:-1]))
    
  trainingRDD, testRDD = labeledRDD.randomSplit([0.7, 0.3])
  
  timeBegin = time.time()
  for i in range(0, NUM_ITERATION):
    model = testTree.trainModel(sc, trainingRDD)
  timeEnd = time.time()
  
  totalTime = timeEnd - timeBegin
  meanTime = totalTime/NUM_ITERATION
  
  print("Total time of training : " + str(totalTime))
  print("Mean time of training : " + str(meanTime))
