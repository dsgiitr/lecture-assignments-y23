import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import numpy as np
# Arguments -> train_path, test_path, criterion, n_estimators, max_depth, pred_path
print()
train = pd.read_csv(sys.argv[1])
test = pd.read_csv(sys.argv[2])
train.info()
test.info()
# Pairplot
print()
sns.pairplot(train, hue = 'target')
plt.show(block=False)
# Imputation
print()
for col in train.columns:
    if (col == 'target'):
        continue
    else:
        overall_mean = train[col].mean()
        train.loc[np.isnan(train[col]), col] = overall_mean
display(train)
# Pipeline and Scaling
print()
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
X = train.drop('target',axis=1)
numeric_pipeline = Pipeline(steps=[("scale", StandardScaler())])
num_cols = X.select_dtypes(include="number").columns
full_processor = ColumnTransformer(transformers=[("num", numeric_pipeline, num_cols)])
# Train-Test Split
print()
from sklearn.model_selection import train_test_split
Xt = full_processor.fit_transform(X)
y = train['target']
X_train, X_test, y_train, y_test = train_test_split(Xt, y, test_size=0.3)
# Random Forest Classifier
print()
from sklearn.ensemble import RandomForestClassifier as rfcl
from sklearn.metrics import classification_report,confusion_matrix
rfc = rfcl(criterion=sys.argv[3], n_estimators=int(sys.argv[4]), max_depth=int(sys.argv[5]))
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
cm = confusion_matrix(y_test,rfc_pred)
cr = classification_report(y_test, rfc_pred)
print(cm)
print(cr)
# Final Model
print()
rfc.fit(Xt, y)
preds = rfc.predict(full_processor.transform(test))
test['target'] = preds
test.to_csv(sys.argv[6], index = False)
