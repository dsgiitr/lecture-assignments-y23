#! /bin/bash

# Training the model

echo -n "Enter the number of epochs for training the model:"
read epochs

echo "Enter the batch size for training the model:"
read batch_size

# Train the model
python train.py --epochs $epochs --batch-size $batch_size &>> outputs.txt


