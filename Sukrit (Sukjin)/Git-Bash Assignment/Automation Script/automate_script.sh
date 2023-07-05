#!/bin/bash

read -p "Enter the path to access the training dataset: " train_path
read -p "Enter the path to access the test dataset: " test_path
read -p "Enter the evalution criterion for the Random Forest Classifier: " criterion
read -p "Enter the number of trees (n_estimators) for the RFC: " n_estimators
read -p "Enter the max tree depth for the RFC: " max_depth
read -p "Enter the path where the prediction should be created or updated: " pred_path
python python_code.py $train_path $test_path $criterion $n_estimators $max_depth $pred_path
