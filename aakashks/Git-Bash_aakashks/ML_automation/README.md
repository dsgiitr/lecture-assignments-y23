# ML automation script using bash and argparse

The script is supposed to take preprocessed csv file paths and fit the model with user defined parameters
then the predictions are output to submissions file and the logs are logged into output.txt.

It uses a Random Forest Classifier on the data. User needs to specify the n_estimators and max_depth
parameters of the sklearn model.
