import sys
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
sc = SparkContext()

def main(inputFile):
  rawRDD = sc.textFile(inputFile)
  labeledRDD = rawRDD.map(lambda line: line.split(','))\
    .map(lambda row: LabeledPoint(row[-1], row[0:-1]))
  cats = {0: 5, 1: 14, 2: 5, 3: 14, 4: 5, 5: 14, 6: 5, 7: 14, 8: 5, 9: 14}
  model = DecisionTree.trainClassifier(labeledRDD, 10, cats, maxDepth=20, maxBins=64)
  return model

if __name__ == "__main__":
  main(sys.argv[1])

