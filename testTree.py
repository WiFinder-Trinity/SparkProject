from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree

def main(sc, inputFile, num_partitions):
  rawRDD = sc.textFile(inputFile, num_partitions)
  labeledRDD = rawRDD.map(lambda line: line.split(','))\
    .map(lambda row: LabeledPoint(row[-1], row[0:-1]))
  cats = {0: 5, 1: 14, 2: 5, 3: 14, 4: 5, 5: 14, 6: 5, 7: 14, 8: 5, 9: 14}
  model = DecisionTree.trainClassifier(labeledRDD, 10, cats, maxDepth=10, maxBins=32)
  return model
  
def trainModel(sc, labeledRDD):
  cats = {0: 5, 1: 14, 2: 5, 3: 14, 4: 5, 5: 14, 6: 5, 7: 14, 8: 5, 9: 14}
  model = DecisionTree.trainClassifier(labeledRDD, 10, cats, maxDepth=15, maxBins=32)
  return model

