# Spark Project
In this project, we try to evaluate the performance of Apache Spark & its MLlib library
in function of different parameters: data size, slave nodes, CPU cores...
Data used in the tests comes from a poker hand data set, and you can find it [here](http://archive.ics.uci.edu/ml/datasets/Poker+Hand).

## Documentation
* `Results` this folder contains our graphs and explainations about our test method.
* `environment.sh` a script you will certainly need to adapt to your Spark installation
 to set the environment variables required to run PySpark.
* `init.sh` An init script to download the data, unzip it and set the environment
* `performance.py` The main script to run
* `testTree.py` The training method of our program
* `training.py` called by `performance.py` to execute the tests and return their results.

Therefore, to run the project:
1. Run `./init.sh`
2. Create a Spark master and slave(s)
3. Run `python performance.py`
