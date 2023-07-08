# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 01:44:31 2023

@author: Shree
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve

np.random.seed(22)

def generate_data(n_dims, n_points, std):
    global coefs
    # equation will be of the form a1x1 + a2x2 + a3x3 ... = 0 forming a hyperplane
    features = np.random.normal(0, std, (n_points, n_dims))
    coefs = np.random.normal(0, std, (1, n_dims))
    print(coefs.flatten())
    # class will be decided based upon the distance and direction from the hyperplane 
    ys = (coefs @ features.T).flatten() + np.random.normal(0, 1, n_points)
        
    return features, ys

n_dims = 10
n_points = 100
std = 5
features, ys = generate_data(n_dims, n_points, std)

plt.scatter(features[:, 0], ys)

# use scipy to solve system of equations
def equation_gen(coefficients):    
    #MLE estimate
    return [np.sum((ys-coefficients[None, :]@features.T)*features[:, j]) for j in range(n_dims)]

def solve(equations):
    solved_coefs = fsolve(equations, np.zeros(n_dims), )
    return solved_coefs.flatten()

solved_coefs = solve(equation_gen)
print(solved_coefs)
plt.plot(features[:, 0], solved_coefs[0]*features[:, 0], c='red')
plt.plot(features[:, 0], coefs[0, 0]*features[:, 0], c='green')