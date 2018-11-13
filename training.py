import testTree

def training(sc, inputFile):
  rawRDD = sc.textFile(inputFile)
  labeledRDD = rawRDD.map(lambda line: line.split(','))\
    .map(lambda row: LabeledPoint(row[-1], row[0:-1]))
    
  trainingRDD, testRDD = labeledRDD.randomSplit(0.7, 0.3)
