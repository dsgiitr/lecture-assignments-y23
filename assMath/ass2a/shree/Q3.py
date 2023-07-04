# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 01:36:31 2023

@author: Shree
"""

import numpy as np

mu = 10
var = 8
n = 69

data = np.random.normal(mu, var**0.5, n)

mle_mu = data.sum()/n
mle_var = ((data-mle_mu)**2).sum()/n

print(f"true mu: {mu}, true variance: {var}")
print(f"estimate mu: {mle_mu}, estimate variance: {mle_var}")