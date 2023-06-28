#!/usr/bin/env bash

count=0
until [[ "$?" -ne 0 ]];
do
   count=$(( count + 1 ))
   ./random.sh &> a.txt
done

echo "error returned after runs : $count"
cat a.txt