import os
import time
import csv
import testTree
import matplotlib.pyplot as plt

NUM_ITERATION = 5
dataFiles = os.listdir("./data")
dataFiles = ["./data/"+i for i in dataFiles]
dataFiles.sort()

stats = []

#MLlib seems to take time to have maximum speed so we "train" it
print('"Trainig" MLLib to get maximum speed')
for i in range(0, NUM_ITERATION):
  testTree.main(dataFiles[0])

print("----------------")
print("Real test begins")
print("----------------")
for it, dataFile in enumerate(dataFiles):
  print("Test with file " + dataFile)
  timeBegin = time.time()
  for i in range(0, NUM_ITERATION):
    testTree.main(dataFile)
  timeEnd = time.time()
  
  totalTime = timeEnd - timeBegin
  meanTime = totalTime/NUM_ITERATION
  
  print("Total time : " + str(totalTime))
  print("Mean time  : " + str(meanTime))
  
  #Compute statistics on dataFile
  size = os.path.getsize(dataFile)
  numLines = sum(1 for line in open(dataFile))
  stats.append([dataFile, size, numLines, meanTime])
  print("----------------")
  
print("Test finished")
print("----------------")
print("Writing results on output.csv")


with open('output.csv', 'w') as o_file:
  o_file.write('#file_name, file_size(octect), number_of_line, mean_time\n')
  wr = csv.writer(o_file)
  wr.writerows(stats)
  
print("Results are written")
