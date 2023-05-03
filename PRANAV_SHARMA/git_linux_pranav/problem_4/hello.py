import sys
import argparse
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import random

parser = argparse.ArgumentParser()
parser.add_argument('data', metavar ='N', 
                    type = int,
                    help ='an integer for the accumulator')
args = parser.parse_args()

n = args.data 
diabetes_x = np.random.randint(1,1000,(n,1))
diabetes_y = np.random.randint(1,1000,(n,1))
diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[-30:]
diabetes_y_train=diabetes_y[:-30]
diabetes_y_test=diabetes_y[-30:]
model=linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)
pre=model.predict(diabetes_x_test)
from sklearn.metrics import mean_squared_error
print("MSE is :", mean_squared_error(diabetes_y_test,pre))
print("Weight :",model.coef_)