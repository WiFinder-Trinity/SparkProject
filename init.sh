#!/bin/bash

pip3 install -r requirements.txt

if [ ! -d "data" ]; then
  wget "https://fex.insa-lyon.fr/get?dlid=qfLwD2RZnay22gjBSzf&auto=1&k=bIqFvkMGwqWcDPGek8p" -O data.zip
  unzip data.zip
  rm data.zip
fi

echo "Init is done, you can use the script !"
