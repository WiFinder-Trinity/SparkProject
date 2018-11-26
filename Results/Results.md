# Spark MLLib : testing the framework

## The data

Data are a set of multiple poker hands labeled with their force.
Each line is composed by 5 doublets of numbers representing one card and the force of the hand.
The doublet looks like : `COLOR, NUMBER`, where `COLOR` is between 1 and 4 and `NUMBER` between 1 and 13.
Force is from 0 (no combination) and 9 (quint flush)

The features of our data is the hand and the label is the force

We made our tests with four increasing size data files  :
1. 4 000 lines (94.1 ko)
2. 25 010 lines (613.7 ko)
3. 100 000 lines (2.4 Mo)
3. 1 000 000 lines (22 Mo)

## Algorithm

We use the MLLib Decision Tree algorithm to train a model to predict the force of a hand.
Parameters of the algorithm are :
* classes to find = 10
* max depth = 15
* maxBins = 32

## Test protocol
During all the tests, 70% of the data set was randomly choose to train the model
and 30% to evaluate it.

Therefore, in our four cases we used for training :
1. 2 800 lines
2. 17 500 lines
3. 70 000 lines
4. 700 000 lines

and for evaluation :
1. 1 200 lines
2. 7 500 lines
3. 30 000 lines
4. 300 000 lines

We performed our deployment on grid5000 in 2 steps
1. On multiple nodes, allocating for each only 15 cores, we ran the algorithm on 1, 2, 4 and 8 nodes.
2. On one unique node, we ran the algorithm allocating 15, 30, 45 and 60 cores.

Each time, the number of partition of the RDD was equal to the total number of cores.
