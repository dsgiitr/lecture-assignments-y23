#!/bin/bash

# this script will be usable to create a dir in which there will be a venv with preloaded packages
# then load the specified kaggle datasets into that folder

# check if argument is provided

if [ $# -eq 0 ]
  then
    echo "No argument provided. Will use default name"
    mkdir test
    venv_name=test
fi

mkdir $1
cd $1
venv_name=$1

# Create virtual environment
python3 -m venv ./.venv
source ./.venv/bin/activate

pip install numpy pandas seaborn matplotlib
pip install kaggle

mkdir data
