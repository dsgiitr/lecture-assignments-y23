#!/bin/bash
rm output.log
rm error.log

touch output.log
touch error.log

while true; do
  bash script.sh >> output.log 2>> error.log
  if [ $? -ne 0 ]; then
    echo "Command failed. Output:"
    cat output.log
    echo "Error:"
    cat error.log

    exit 0
  fi
done
