#!/bin/bash

echo "In the PATH variable, do not forget to add the bin of spark that you must install"

echo "Some environment variables has to be add"
export PYSPARK_PYTHON=python3
echo "PYSPARK_PYTHON is added"

sudo pip3 install -r requirements.txt

if [ ! -d "data" ]; then
  wget "https://fex.insa-lyon.fr/get?dlid=qfLwD2RZnay22gjBSzf&auto=1&k=bIqFvkMGwqWcDPGek8p" -O data.zip
  unzip data.zip
  rm data.zip
fi

echo "Init is done, you can use the script !"
