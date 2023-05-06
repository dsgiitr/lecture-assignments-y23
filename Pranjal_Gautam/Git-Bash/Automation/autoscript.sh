#!/bin/env bash

read -p "Enter Kaggle dataset API key: " api_key
$api_key

find . -type f -name "*.zip" | xargs unzip -d ./Datasets
find ./Datasets -name "*.csv" | while read filename; do mv "$filename" "$(echo $filename | sed 's/ /_/g')"; done
dir=$(find ./Datasets -type f -name "*.csv")
read -p "1: Regression 2: Classification " type1
read -p "No. of epochs " type2
read -p "Learning rate " type3
read -p "Batch size " type4
read -p "Directory to testing data " type5
python3 ./torchie.py $dir $type1 $type2 $type3 $type4 $type5

find . -type f -name "*.zip" | xargs rm -rf
rm -rf ./Datasets
mkdir ./Datasets
