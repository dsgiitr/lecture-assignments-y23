#!/usr/bin/env bash

n=0

while [[ true ]]
do
        ((n++))
        ./error.sh >> stdout.txt 2>> stderr.txt
        if [[ $? -ne 0 ]]; then
		echo "Error detected in $n th try"
                break
        fi
done

