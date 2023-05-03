import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--train-data')
parser.add_argument('-t', '--test-data')
parser.add_argument('-f', '--target-feature')
parser.add_argument('-p', '--parameters', nargs=2, type=int)

args = parser.parse_args()

# Assuming that the data file train_data is preprocessed
train_data = pd.read_csv(args.train_data_path)
test_data = pd.read_csv(args.test_data_path)

# Separating X and y
y = train_data[args.target_feature]
X = train_data.drop(args.target_feature)
X_test = test_data.drop(args.target_feature)

model = RandomForestClassifier(
    n_estimators=args.parameters[0],
    max_depth=args.parameters[1],
    random_state=42
)

print('Fitting model')
model.fit(X, y)

print('generating predictions')
predictions = model.predict(X_test)
output_predictions = pd.DataFrame(
    {'ID': test_data.index, args.target_feature: predictions}
)

print('Saving predictions in a file')
output_predictions.to_csv('./submissions.csv', index=False)