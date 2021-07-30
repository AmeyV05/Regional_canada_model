#! /bin/bash

for FILE in $(cat ./cpfiles.txt)
do 
  pathfile="$1"/${FILE}
  scp -r vasulkar@cartesius.surfsara.nl:$pathfile "$2"
done