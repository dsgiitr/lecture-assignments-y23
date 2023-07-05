# 2DRandomWalk
```
Uses random function to get a value in the range [0,2pi]
Moves the position in the 2d space using sin and cos function
plots the final position after 100 steps
Note: Result looks like probability density of 2d functions (2d electron density).
```
# InputRandomWalk
```
Takes user input for the number of possible steps, and each step.
For example:
3
-4
5
1
Means that there are 3 possible steps of distance (3,-4,5).
Maps out the distribution and finds out the mean and standard deviation in the distribution of final positions.
```
# NormalDistribution
```
Position starts from 0 and a random variable is added to the current position, where the random variable is based on a normal distribution.
Then the path of position is mapped out for multiple loops.
```
# RandomWalk
```
Runs a lot of loops of random walks of 100 steps and maps final position of each of them in a position-frequency graph. This distribution matches a normal distribution.
```
# RandoWalkSTD
```
The distributions are calculated, and the mean and standard deviation is found out for varying amount of steps. The standard deviations for each distribution is mapped along with the no of steps for each. This shows that the standard deviation is proportional to the square of the number of steps in each loop (or that the variance is proportional to the number of steps).
```