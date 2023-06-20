# Statistics and Probability Assignment.
Starting with some good questions covering basic statistics of machine learning,

1. Let $X \leftarrow P(x) = e^{-\lambda} \frac{\lambda^x}{x!}$ and $Y \leftarrow P(y) = e^{-\mu} \frac{\mu^y}{y!}$ and assume that $X$ and $Y$ are independent. Show that the distribution of $X$ given that $X + Y = n$ is  ${n \choose k} \pi^x (1-\pi)^{n-x}$ where $\pi = \frac{\lambda}{\lambda + \mu}$

2. Let $X_1, X_2, X_3, ...$ be a sequence of random variables such that
$$P(X_n = \frac{1}{n}) = 1 - \frac{1}{n^2}$$$$P(X_n = n) = \frac{1}{n^2}$$
Does $X_n$ converge in probability? Does $X_n$ converge in quadratic mean?

3. Let $X$ be a continuous random variable with Cumulative Distribution Function F. Suppose that $P(X>0) = 1$ and that $E(X)$ exists. Show that $E(X) = \int_{0}^{\infty}P(X>x)dx$.

4. Evaluate the Kellback-Leibler divergence between two Gaussains $p(x) = \mathcal{N}(x|\mu, E)$ and $q(x) = \mathcal{N}(x|m,L).$

5. If $(X,Y)$ has the bivariate normal probability distribution function,
$$f(X,Y) = \frac{1}{2\pi(1-\rho^2)^{1/2}} exp\left(\frac{-1}{2(1-\rho^2)} (x^2 - 2\rho xy + y^2) \right)$$
show that $Corr(X,Y) = \rho$ and $Corr(X^2,Y^2) = \rho^2$.

6. Let $X$ have the gamma distribution with parameters $n$ and $3$, where $n$ is a large integer. Explain how Central Limit Theorem can approximate the distribution of $X$ by a normal distribution. Also find which normal distribution approximates the distribution of $X$?


Now, statistics is obviously a integral part of Machine learning and serves as it's foundation. But it is not the only place it used, one of it's application is Filters.

## What are filters?
A filter is an efficient optimal estimator (a set of mathematical equations) that provides a recursive computational methodology for estimating the state of a discrete-data controlled process from measurements that are typically noisy, while providing an estimate of the uncertainty of the estimates.

What it means in English is that, give this filter a series of noisy data filter will give you the best estimate of the true data along with a measure of uncertainity.

Most Famous of such filters is Kalmann filter, You can read about it [here](https://web.mit.edu/kirtley/kirtley/binlustuff/literature/control/Kalman%20filter.pdf), for intutive undersstanding look [here](https://www.kalmanfilter.net/default.aspx) and [here](https://www.analyticsvidhya.com/blog/2021/10/an-intuition-about-kalman-filter/). Kalmann filter is used in many places such as Finance, Robotics and most important of all (for you) Computer vision.

So what you have to do for this assignment is create a human tracking system using YOLO.

## How to go about doing it?
First things first, what is YOLO? In case you don't know what is yolo, don't worry Yolo in it's base form is an object detection model. You don't have to worry much about that I have provided you with the code base [here](https://github.com/PriyanshuPansari/kalman_filter_assignment) and the only thing you have to do is implemnt the kalman filter in Kalman_filter.py to predict the future state of bounding box.

What YOLO gives is a bounding box, which effectively is a rectangular shape that is used to enclose and define the spatial extent of an object or region of interest, in this case you will be getting 2 points specifying top-left most corner of the box and two values specifying width and height of the box.

Now that you know what to do, How will you do it? Well thats on you, But the only thing you have to make sure about is that each class function is doing what it is supposed to do based on the comments.

Tip- Think about what is the state space that you are trying to estimate?

