#!/usr/bin/env bash

count=0
until [[ "$?" -ne 0 ]];
do
   count=$(( count + 1 ))
   ./random.sh &> output.txt
done

echo "found error after $count runs"
cat output.txt
