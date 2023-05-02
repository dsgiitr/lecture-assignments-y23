#!/bin/bash
Dataset_name=melbourne-housing-snapshot
kaggle datasets download -d dansbecker/melbourne-housing-snapshot
#kaggle api must be iinstalled and kaggle.json muct be in ~/kaggle/
# Extract the downloaded dataset
unzip "$DATASET_NAME.zip"

python train.py --data_path "$DATASET_NAME"