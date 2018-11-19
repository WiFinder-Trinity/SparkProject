from pyspark import SparkContext
import os
import csv
import testTree
import training

sc = SparkContext()

NB_PARTITIONS = sc.defaultParallelism

with open('output.csv', 'w') as o_file:
  o_file.write('#file_name, file_size(octect), number_of_line, mean_time_training, accuracy\n')

dataFiles = os.listdir("./data")
dataFiles = ["./data/"+i for i in dataFiles]
dataFiles.sort()

#MLlib seems to take time to have maximum speed so we "train" it
print('"Warming up" MLLib to get maximum speed')
for i in range(0, 5):
  testTree.main(sc, dataFiles[0])

print("----------------")
print("Real test begins")
print("----------------")
for it, dataFile in enumerate(dataFiles):
  stats = []  
  partialStat = training.training(sc, dataFile, NB_PARTITIONS)
  
  #Compute statistics on dataFile
  size = os.path.getsize(dataFile)
  numLines = sum(1 for line in open(dataFile))
  stats += [dataFile, size, numLines]
  stats += partialStat
  with open('output.csv', 'a') as o_file:
    wr = csv.writer(o_file)
    wr.writerow(stats)
  print("----------------")
  
print("Test finished")
print("----------------")
print("Writing results on output.csv")
  
print("Results are written")
