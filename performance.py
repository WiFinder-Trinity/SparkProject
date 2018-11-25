from pyspark import SparkContext
import sys
import os
import csv
import testTree
import training

sc = SparkContext()


if(len(sys.argv) < 3): 
  print("please give an output file");
  exit()

OUTPUT_FILE = sys.argv[1]
NB_PARTITIONS = int(sys.argv[2])

print(NB_PARTITIONS)

with open(OUTPUT_FILE, 'w') as o_file:
  o_file.write('#file_name, file_size(octect), number_of_lines_model, number_of_lines_test, mean_time_training, mean_time_prediction, accuracy\n')

dataFiles = os.listdir("./data")
dataFiles = ["./data/"+i for i in dataFiles]
dataFiles.sort()

#MLlib seems to take time to have maximum speed so we "train" it
print('"Warming up" MLLib to get maximum speed')
for i in range(0, 5):
  testTree.main(sc, dataFiles[0], NB_PARTITIONS)

print("----------------")
print("Real test begins")
print("----------------")
for it, dataFile in enumerate(dataFiles):
  stats = []  
  partialStat = training.training(sc, dataFile, NB_PARTITIONS)
  
  #Compute statistics on dataFile
  size = os.path.getsize(dataFile)
  stats += [dataFile, size]
  stats += partialStat
  with open(OUTPUT_FILE, 'a') as o_file:
    wr = csv.writer(o_file)
    wr.writerow(stats)
  print("----------------")
  
print("Test finished")
print("----------------")
print("Writing results on " + OUTPUT_FILE)
