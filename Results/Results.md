# Spark MLlib : testing the framework

## The data
We made our tests with four increazing size data files  :
1. 4 000 lines (94.1 ko)
2. 25 010 lines (613.7 ko)
3. 100 000 lines (2.4 Mo)
3. 1 000 000 lines (22 Mo)

## Algorithm

## Test protocol
During all the tests, 70% of the dataset was randomly choose to train the model
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
