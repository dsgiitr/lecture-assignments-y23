# Prob Stats pre lecture

## Random walk

A purely random walk with epsiloni is a randomly -1 or 1
we are generating a random variable X's path

![random_walk](/aakashks/assets/img/output.png "Random Walk")

## Irregular walk

here we have set the probability of going towards one side is higher.
hence, for a bigger path it eventually becomes a straight line

![irregular_walk](/aakashks/assets/img/output1.png "irregular walk")

## Central Limit theorem

ran multiple walks and
plotted the frequency that a particular point in the
2d space is reached in the walks.
proof of central limit theorem as the no of the
random walks increases

![CLT](/aakashks/assets/img/output2.png)

## Poisson process

Random walk such that Xi+1 - Xi = ei
and ei ~ exp(1/lambda)

so now X will represent a stochastic process (which is poisson process)

![Poisson_process](/aakashks/assets/img/output4.png)

## 2D Random Walk

Xi+1 = Xi + exp(i:theta:)
radially the theta is varying randomly
formally, theta ~ uniform(0, 2pi)
then we get a random walk.
