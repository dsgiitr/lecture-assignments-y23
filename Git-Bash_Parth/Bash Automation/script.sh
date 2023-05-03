#!bin/bash

#pip3 install requirements.txt

echo -n "Enter a link to dataset : "
read dataset

wget $dataset -O "dataset/file.txt"

echo -n "Enter the number of epochs : "
read epochs

echo -n "Enter the batch size : "
read batch_size

echo -n "Enter project name : "
read project

echo -n "Enter name of the dataset : "
read dataset

echo "
Project : $project
Dataset : $dataset
" > curr_run

wandb login

python3 train.py $epochs $batch_size $project $dataset


