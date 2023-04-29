#!/bin/env bash
count=0
while [[ "$?" -eq 0 ]];
do
count=$(( count+1 )) 
./problem.sh &> output.txt 
done
echo "error after $count runs"
cat output.txt

