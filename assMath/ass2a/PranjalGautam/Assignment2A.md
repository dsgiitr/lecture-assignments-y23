# Assignment 2A

-By Pranjal Gautam

# Q1

$$
P(X=k)=(\frac {\lambda^k} {k!})e^{-\lambda}
$$

For Alice,

$$
\lambda=10
$$

And for bob,

$$
\lambda=15
$$

The posterior odds that Alice is filling in for Bob is given by

$$
\frac {P(A|x)} {P(B|x)}
$$

Where P(A) is the conditional probability of Alice working given the data x=[12,10,11,4,11].

Now,

$$
P(A|x)=\frac {P(x|A)P(A)} {P(x)}
$$

$$
P(A|x)=\frac {\frac {1} {11}(\frac {10^{12}} {12!}e^{-10}).(\frac {10^{11}} {11!}e^{-10}).(\frac {10^{10}} {10!}e^{-10}).(\frac {10^{4}} {4!}e^{-10}).(\frac {10^{11}} {11!}e^{-10})} {\frac {1} {11}(\frac {10^{12}} {12!}e^{-10}).(\frac {10^{11}} {11!}e^{-10}).(\frac {10^{10}} {10!}e^{-10}).(\frac {10^{4}} {4!}e^{-10}).(\frac {10^{11}} {11!}e^{-10})+\frac {10} {11}(\frac {15^{12}} {12!}e^{-15}).(\frac {15^{11}} {11!}e^{-15}).(\frac {15^{10}} {10!}e^{-15}).(\frac {15^{4}} {4!}e^{-15}).(\frac {15^{11}} {11!}e^{-15})}
$$

From this, we get posterior odds:

$$
P(A|x)=\frac {10^{48}} {10\cdot15^{48}\cdot e^{-25}}
$$

$$
P(A|x)=\frac {10^{47}} {15^{48}\cdot e^{-25}}
$$

This is approximately equal to 25.4

# Q2

### (a)

We know, 

$$
\theta \thicksim N(5,9)
$$

$$
x \thicksim N(\theta,4)
$$

Where N is the Gaussian Distribution.

Now, from the definition of Gaussian Distribution,

$$
P(x|\theta)=\frac {1} {2\sqrt{2\pi}}e^{-\frac {1} 2 (\frac {x-\theta} {2})^2}
$$

Now, using Bayes’ Theorem,

$$
P(\theta|x)=\frac {P(x|\theta)P(\theta)} {P(x)}
$$

$$
P(\theta)=\frac {1} {3\sqrt{2\pi}}e^{-\frac {1} 2 (\frac {\theta-5} {3})^2}
$$

We need to find:

$$
arg max(P(\theta|x)) 
$$

$$
=argmax(log(P(x|\theta) + log(P(\theta)))
$$

$$
=argmax(-\frac 1 2(\frac {6-\theta} {2})^2-\frac 1 2 (\frac {\theta-5} {3})^2)
$$

Using differentiation and setting to 0

$$
\frac {\delta l(\theta)} {\delta \theta}=0
$$

we get

$$
\theta= \frac {74} {13}
$$

So,

$$
\theta \thicksim N(\frac {74} {13}, \sigma^2)
$$

We know for sigma2

$$
\sigma^2=E[(\theta-posterior\_mean)^2∣x]
$$


$$
\sigma^2=(prior\_var*likelihood\_var)/(prior\_var+likelihood\_var)
$$

plugging in the values we get,

$$
\sigma^2=(9*4)/(9+4) \newline\sigma^2=\frac {36} {13} 
$$

So,

$$
\theta \thicksim N(\frac {74} {13}, \frac {36} {13})
$$

### (b)

We know,

$$
n=4\newline \bar{x}=6\newline prior(\theta)\thicksim N(5,9)\newline x \thicksim N(\theta,4) \newline \mu_{posterior}=\frac {\frac {\mu_{prior}} {\sigma^2_{prior}}+\frac {n\bar{x}} {\sigma^2}} {\frac 1 {\sigma^2_{prior}}+\frac n {\sigma^2}} \newline \sigma^2_{posterior}= \frac 1 {\frac 1 {\sigma^2_{prior}}+\frac n {\sigma^2}}
$$

Now,

$$
posterior(\theta)\thicksim N(\mu_{posterior},\sigma^2_{posterior})
\newline
\mu_{posterior}=\frac {(\frac {5} {9}+\frac {4\cdot6} {4})} {\frac 1 9+\frac 4 4}
\newline 
\mu_{posterior}=\frac {59} {10}=5.9
\newline
\sigma^2_{posterior}=\frac 1 {\frac 1 9 + \frac 4 4}=\frac 9 {10}=0.9
$$

So,

$$
posterior(\theta)\thicksim N(5.9,0.9)
$$

We can see that as n increases, the variance in the posterior decreases, so we get more certain (confident) in our answer. Also, as n increases, the weight given to the sample mean also increases, that means we tend to believe our value is closer to the sample mean than the prior mean. We get x=6 4 times in a row and the distribution tends towards 6 more than it is towards the prior mean 5.

### (c)

As I mentioned in part b, lets look at the equations again.

$$
\mu_{posterior}=\frac {\frac {\mu_{prior}} {\sigma^2_{prior}}+\frac {n\bar{x}} {\sigma^2}} {\alpha} \newline \sigma^2_{posterior}= \frac 1 {\alpha}\newline \alpha= {\frac 1 {\sigma^2_{prior}}+\frac n {\sigma^2}}
$$

Here we note two interesting things. First, our posterior variance only depends on alpha, which in turn depends on the prior variance, variance in the distribution of x, and most interestingly, n. As we have more samples, n increases, and the posterior variance decreases. This means we become more certain about the accuracy of our estimate as we get newer information.

Assuming our prior mean to be constant, we can observe that as we obtain more samples, the mean of our estimate converges towards the sample mean. This indicates that we become less certain about our initial estimates and rely more on the information provided by the new data. In a sense, the posterior is a self-correcting estimate that balances both prior knowledge and new data, and provides an estimate of the true data accordingly.

### (d)(i)

Let the true IQ be theta, then the test follows

$$
X\thicksim N(\theta, 102)\newline prior(\theta) \thicksim N(100,152)
\newline
X=80
$$

We can easily use these values to get posterior mean and variance

$$
\mu_{posterior}=\frac {\frac {100} {152}+\frac {80} {102}} {\frac 1 {152}+\frac 1 {102}}=88.031
\newline
\sigma^2_{posterior}=\frac 1 {\frac 1 {102}+ \frac 1 {152}}=61.039
$$

So we can say the expected value of his IQ

$$
E[x]=\mu_{posterior}=88.031
$$

### (ii)

Similarly for the second case,

$$
X\thicksim N(\theta, 102)\newline prior(\theta) \thicksim N(100,152)
\newline
X=150
$$

$$
\mu_{posterior}=\frac {\frac {100} {152}+\frac {150} {102}} {\frac 1 {152}+\frac 1 {102}}=129.921
\newline
\sigma^2_{posterior}=\frac 1 {\frac 1 {102}+ \frac 1 {152}}=61.039
$$

So the expected value

$$
E[x]=\mu_{posterior}=129.921
$$

# Q5

### a.

For a constant function, we can clearly see that the vc dimension is 1 as it can only classify one point as different then all other points.

### b.

For a linear function in d dimensions, 

$$
f(x)=\theta_1x_1+\theta_2x_2...+\theta_dx_d+\theta_0
$$

We can clearly see that the maximum d+1, since we can only differentiate between a maximum of d+1 points, one for each unique feature.

### c.

For an axis aligned rectangle in two dimensions:
If it is aligned in two dimensions, the vc dimension is 1.
Otherwise, if it is only aligned in one dimension with the axis, the answer is 4. 

### d.

For an interval, we can see the vc dimension is 2, since if there are three points in increasing order, it can never classify {1,3} and {2} differently.