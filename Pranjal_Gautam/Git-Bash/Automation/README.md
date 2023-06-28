# Bash script
```
Takes the input:
->API key for kaggle dataset download
->Whether the model is for classification or regression
->Number of epochs
->Learning rate
->Batch size
->Path to testing data
It downloads the dataset, unzips the file, adds the csv file to the dataset folder, and then passes all inputs along with the path to the csv files
After the python script finishes running, it deletes the zip and csv file downloaded to keep the folder clean.
DO NOT STORE ANY IMPORTANT ZIP OR CSV FILE IN THE SAME FOLDER AS THE SCRIPT WHILE RUNNING IT
```

# Python script
```
Takes in the input and assigns them to variables using the sys module. 
Makes a simple 4 layer neural network based on the type of model.
Trains a model using the downloaded dataset and uses it to evaluate the given csv file.
stores the output in a file called output.csv
```