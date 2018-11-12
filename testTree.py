import sys
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
sc = SparkContext()

def main(inputFile):
  rawRDD = sc.textFile(inputFile)
  labeledRDD = rawRDD.map(lambda line: line.split(','))\
    .map(lambda row: LabeledPoint(row[-1], row[0:-1]))
  model = DecisionTree.trainClassifier(labeledRDD, 10, {}, maxDepth=10)

if __name__ == "__main__":
  main(sys.argv[1])

