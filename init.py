from pyspark import SparkContext

sparkProtocol = "spark://"
port = ":7077"

def initSparkContext(masterAddress):
  sc = SparkContext(spark + masterAddress + port)
  return sc

