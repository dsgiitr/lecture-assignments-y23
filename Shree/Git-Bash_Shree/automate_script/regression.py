import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# command line arguments
n = int(sys.argv[1])
degree = int(sys.argv[2])

x = np.array(sorted(random.sample(range(-50, 51), n)))
y = np.zeros(n)
for i in range(degree + 1):
    y += np.random.normal(scale=2**(-i), size=n) * (x ** i)

poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(x.reshape(-1, 1))
regressor = LinearRegression()
regressor.fit(X_poly, y)

plt.scatter(x, y)
plt.plot(x, regressor.predict(X_poly), color='red')
plt.title(f"Polynomial Regression (degree={degree}, n={n})")
plt.show()

