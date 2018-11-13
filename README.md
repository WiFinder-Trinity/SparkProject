# Spark Project

In order to get the data used for the project, go to this link
: [data](https://fex.insa-lyon.fr/get?k=bIqFvkMGwqWcDPGek8p)

You will download a zip archive that you will have to unzip at the root of the
repositiory

## Documentation
* `init.sh` An init script to download the data and set the environment
* `performance.py` The main file to run
* `init.py` Init the configuration of the master node
* `testTree.py` The training method of our program
* `wordcount.py` a file created to test and familiarize ourselves with Spark, useless now

Therefore, to run the project:
1. `./init.sh`
2. Create Spark master and slaves
3. `python performance.py`
