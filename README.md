# Spark Project
In this project, we use a poker hand data set, you can download it with this [link](https://fex.insa-lyon.fr/get?k=bIqFvkMGwqWcDPGek8p).

## Documentation
* `init.sh` An init script to download the data, unzip it and set the environment
* `performance.py` The main file to run
* `init.py` Init the configuration of the master node
* `testTree.py` The training method of our program
* `wordcount.py` (Useless) a file created to test and familiarize ourselves with Spark

Therefore, to run the project:
1. Run `./init.sh`
2. Create a Spark master and slave(s)
3. Run `python performance.py`
