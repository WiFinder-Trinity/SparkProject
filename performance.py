import os
import time
import testTree
import matplotlib.pyplot as plt

NUM_ITERATION = 5
dataFiles = os.listdir("./data")
dataFiles = ["./data/"+i for i in dataFiles]
dataFiles.sort()

timeMeasure = []
x = []


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
  timeMeasure.append(meanTime)
  x.append(it)
  print("----------------")
  
print("Test finished")
  
plt.bar(x, timeMeasure)
plt.show()
