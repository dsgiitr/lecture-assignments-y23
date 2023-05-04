#!/usr/bin/env bash

timesran=1
./rand.sh &> outputs.txt


while [[ $? -ne 1 ]]
do
	timesran=$(( $timesran + 1 ))
	./rand.sh &>> outputs.txt
done

echo -e "the outputs are:\n$(cat outputs.txt)"
echo "the number of times the command ran is $timesran" 

