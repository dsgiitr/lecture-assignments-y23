# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 01:44:31 2023

@author: Shree
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve

np.random.seed(89)
sigmoid = lambda x: 1 / (1 + np.exp(-x))

def generate_data(n_dims, n_points, std):
    global coefs
    # equation will be of the form a1x1 + a2x2 + a3x3 ... = 0 forming a hyperplane
    features = np.random.normal(0, std, (n_points, n_dims))
    coefs = np.random.normal(0, std, (n_dims, 1))
    
    # class will be decided based upon the distance and direction from the hyperplane 
    dists = features @ coefs
    classes = np.random.binomial(1, sigmoid(dists))
    
    print(coefs)
    
    return features, classes.flatten()

n_dims = 5
n_points = 100
std = 2
features, classes = generate_data(n_dims, n_points, std)

plt.scatter(features[:, 0], features[:, 1], c=["orange" if x else "blue" for x in classes])

# use scipy to solve system of equations
coeefs = np.ones((n_dims, 1))
def equation_gen(coefficients):
    
    sigmoids = sigmoid(features @ coefficients)
    
    #MLE estimate
    return [np.sum(features[:, j] * (classes-sigmoids)) for j in range(n_dims)]

    #MAP estimate
    return [np.sum( -coeefs[j]/std**2 + features[:, j] * (classes-sigmoids)) for j in range(n_dims)]

    #MLE performs better than MAP for some reason... I cant tell

def solve(equations):
    solved_coefs = fsolve(equations, np.zeros(n_dims), )
    return solved_coefs
    

solved_coefs = solve(equation_gen)
print(solved_coefs)
plt.plot(features[:, 0], -solved_coefs[0]*features[:, 0]/solved_coefs[1], c='red')
plt.plot(features[:, 0], -coefs[0]*features[:, 0]/coefs[1], c='green')
