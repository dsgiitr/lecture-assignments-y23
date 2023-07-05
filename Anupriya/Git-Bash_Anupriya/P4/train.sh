#!/bin/bash

#using kaggle datasets download -d aymenkhouja/timeofdaydataset as sample dataset
# getting api command from kaggle and downloading zip

echo "Enter Kaggle API command for chosen dataset: "
read apicommand
$apicommand

#after downloading the dataset zip file, we need to unzip it.

echo "Deleting previous stored datasets..."
rm -rf dataset

find . -type f -name "*.zip" | xargs unzip -d ./dataset
find . -type f -name "*.zip" | xargs rm -rf

echo "Enter batch size, Enter number of epochs and number of classes (seperated by spaces)"
#here, using read input works as long as we type cast the sys.argvs values cause they're reading it as a string value cause we have a file name there too.
read -a input

python train_ds.py --batch ${input[0]} --epochs ${input[1]} --classes ${input[2]}

