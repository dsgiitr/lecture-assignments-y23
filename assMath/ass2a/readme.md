# Assignment 2A

1. A local theatre employs two ticket collectors, Alice and Bob, although only one of them
works on any given day. The number of tickets X that a ticket collector can collect in an hour
is modelled by a distribution which has mean λ, and probability mass function

P(X = k) = (λ
k
/k!)e-λ

for k = 0, 1, 2,.... (This distribution is called a Poisson distribution. It is an important discrete
distribution in biology and physics.) Suppose that Alice collects, on average, 10 tickets an
hour and Bob collects, on average, 15 tickets an hour. One day the manager stays home sick.
He knows Bob is supposed to work that day, but thinks there are 1 to 10 odds that Alice is
filling in for Bob (based on Bob’s prior history of taking advantage of Alice’s generous nature
when the manager is away). The suspicious manager monitors ticket sales online and
observes that over the span of 5 hours there are 12, 10, 11, 4, and 11 tickets collected. What
are the manager’s posterior odds that Alice is filling in for Bob?
2. Your friend transmits an unknown value θ to you over a noisy channel. The noise is normally
distributed with mean 0 and a known variance 4. so the value x that you receive is modelled
by N(θ, 4). Based on previous communications, your prior on θ is N(5, 9).
(a) Suppose your friend transmits a value to you that you receive as x = 6. Show that

the posterior pdf for θ is N(74/13, 36/13). The reading gave formulas for normal-
normal updating, but for this problem carry out the calculations from scratch using

our usual Bayesian update table and a good dose of algebra.
(b) Suppose your friend transmits the same value θ to you n times. You receive these

signals plus noise as x1,...,xn with sample mean x ̄. In the reading we gave normal-
normal Bayesian update formulas which apply in this case. For this problem you can

use these formulas.

Suppose your friend transmits the same value θ to you 4 times. You receive these
signals plus noise as x1,...,x4 with sample mean x ̄ = 6. Using the same prior and
know variance σ2 as in part (a), show that the posterior on θ is N(5.9, 0.9). Plot the
prior and posterior on the same graph. Describe how the data changes your belief
about the true value of θ.
(c) How do the mean and variance of the posterior change as more data is received?
What is gained by sending the same signal multiple times? Here we want you to
interpret the equations (1).
(d) IQ in the general population follows a N(100, 152) distribution. An IQ test is
unbiased with a known normal variance of 102; that is, if the same person is tested
multiple times, their measured IQ will differ from their true IQ according to a normal
distribution with mean 0 and variance 100.
i) Randall Vard scored an 80 on the test. What is the expected value of his true IQ?

ii) Mary I. Taft scored a 150 on the test. What is the expected value of her true IQ?
3. Suppose you have a dataset of observations following a Gaussian distribution with an
unknown mean and variance. How would you use MLE to estimate the parameters of the
Gaussian distribution in Python?
4. Suppose you have a dataset of binary classification, and you want to estimate the
parameters of a logistic regression model using MAP estimation with a Gaussian prior on the
model parameters. How would you formulate the likelihood, prior, and posterior
distributions, and how would you find the MAP estimate of the model parameters in
Python?
5. Calculate the VC dimension of the following concept classes(These are fairly trivial cases, I
just want you to have another look at VC dimension):
a. Constant function
b. Linear Function in d dimensions
c. Axis aligned rectangle in 2 dimensions
d. Intervals
Go through these links (reading assignment, lol)

(Compulsory) https://stats.stackexchange.com/questions/182685/why-is-vc-dimension-
important

(For people who like math) https://www.cs.columbia.edu/~verma/classes/ml/ref/lec6_vc.pdf
BONUS QUESTION: This is an OPEN-ENDED question and you are supposed to think in depth about
this one.
We have 2 different Gaussian Distributions D1 and D2 and 2 different datasets, each consisting of N
data points were generated from each distribution, unfortunately the 2 datasets were mixed and
now we have a single dataset consisting of 2N data points. Your job is to figure out the mean and
variance of D1 and D2.
(Note: The combined dataset has equal number of points from D1 and D2, and both the
distributions are Gaussian)
i) Try to devise an algorithm/strategy which can achieve this task, try to prove its
correctness and convergence (if possible)

ii) I am attaching the link of a dataset which has been generated in the above-
mentioned format, figure out the mean and variance of the distributions.

iii) If you think that this cannot be predicted with high certainty using any ML algorithm,
prove it!
iv) Alternatively, consider an easier problem, what if I tell you the distributions D1 and
D2 but make no comment about the ratio of data points taken from each distribution
(like let’s say I take 3 points from D1 for every point taken from D2), can you predict
this ratio? If yes, mention the strategy you will employ.
