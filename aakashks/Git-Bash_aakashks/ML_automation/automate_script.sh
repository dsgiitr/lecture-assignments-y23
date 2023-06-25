#!/bin/bash

output_path=./output.txt

# Getting input from user
echo 'path of training data: '
read train_data_path
echo 'path of test data: '
read test_data_path

read -p 'target feature name: ' target_feature
read -p 'model parameters: ' n_estimators max_depth

# Running python script
python ML_script.py -d $train_data_path -t $test_data_path \
 -f $target_feature -p $n_estimators $max_depth &> $output_path
