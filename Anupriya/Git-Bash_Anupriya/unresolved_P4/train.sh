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
read input

python train_ds.py $input

