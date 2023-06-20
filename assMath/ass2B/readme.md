# Assignment 2B

Q1: a) We usually estimate the mean of the distribution $p(y|x)$, why ?. 

b) In vanilla Linear Regression, we consider $p(y|x) = \mathcal{N}(y; \mu, \sigma)$ we usually take $\mu = w*x$ and $\sigma = I$. Code a vanilla linear regression under this setting. Discuss the effect of choice of sigma over final objective. Is parameterizing sigma really helpful? Explain. 

c) Consider any Exponential family distribution and create a regression model from that. Clearly state what you are trying to estimate. Obtain a loss function for it and generate a simple dataset corresponding to it. Train the corresponding regression model on the created dataset. 

**Note:** For this part you need to code your model from scratch.


Q2 : You are given 2 varibles x and y and corresponding to them you are given 3 different train sets and test sets. Their name is A, B, C. Out of these three one train set and one test set is from the actual data distribution without any errors. Train 3 different linear regression models using [this](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html). Your task is to determine from the given datasets which set is from the actual distribution by assessing each model on each type of test set. For the other datasets find out how do the differ from the actual data distribution. Plot the error terms of these datasets and determine its distribution type and parameters. You might use scikitlearn's Mean Squared Error functions or Mean Absolute Error. Dataset can be found [here](https://drive.google.com/drive/folders/1MiN546HNZm6EKa1Mj3vP3ZeETHIZI3B0?usp=sharing).

**Note:** The dataset whose files name is A in test set as well as train set may not correspond to the same data distribution. 


Q3 : Implement logistic regression from scratch. Generate your custom toy dataset for the same using NumPy. Taking the log likelihood loss function $l(\theta$), use 2 iterative optimization algorithms, (a) Batch Gradient Descent and (b) Fisher scoring (Newton's method) for minimising the loss. Code both these algorithms from scratch too and derive important comparative conclusions from the 2 optimization techniques over the same training dataset (example- convergence speed, runtime complexity etc.) and represent them in any way you like.

*Reading link for [Fisher scoring method](https://hua-zhou.github.io/teaching/biostatm280-2017spring/slides/18-newton/newton.html). You may also refer CS229 notes (topic 7) to read about this.
(**Please note:** Do not use any pre-defined Python class to code any part of the above question such as the ones in Sklearn. The solution should be a step-wise version coded by you representing the mathematical aspect of each step. You can, however use Sklearn for quantifying the comparative conclusions if you wish.)

Q 4: For each of parts, indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer using concepts covered during the lecture and try to hit upon certain key-terms. Also, discuss the bias and variance tradeoff in each scenario.
a. The sample size n is extremely large, and the number of predictors p is small.
b. The number of predictors p is extremely large, and the number of observations n is small.
c. The relationship between the predictors and response is highly non-linear.

**You have to submit your solutions in a Jupyter Notebook. For theretical questions ypu have to use markdown in the notebook itself. Explain things clearly and provide comments wherever you seem necessary.**


