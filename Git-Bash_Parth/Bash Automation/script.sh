#!bin/bash

echo -n "Enter a link to dataset : "
read dataset

wget $dataset -O "dataset/file.txt"

echo -n "Enter the number of epochs : "
read epochs

echo -n "Enter the batch size : "
read batch_size

echo -n "Enter number of heads : "
read heads

echo -n "Enter number of layers : "
read layers

echo -n "Enter block_size / context length : "
read block_size

echo -n "Enter project name : "
read project

echo -n "Enter name of the dataset : "
read dataset

echo "{'Project' : '$project','Dataset' : '$dataset','Num_heads' : '$heads','Num_layers' : '$layers', 'block_size' : '$block_size'}" > curr_run

wandb login

python3 train.py $epochs $batch_size $project $dataset $heads $layers $block_size


