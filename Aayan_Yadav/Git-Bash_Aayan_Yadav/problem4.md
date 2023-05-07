Prerequisite : conda environment initialized in repository 

We automate training of neural network using bash script . The neural network to be trained is stored in neural.py We use `sys` package of python to take inputs of two variables x and y. First we import sys package by `import sys` . It creates a list called sys.argv with filename at 0th index and successive arguments at successive indices. So we put sys.argv[1] as values of x and sys.argv[2] as value of y.

In bash script we run python. The required bash script is given in runner.sh. $1 and $2 are used to pass 1st and 2nd arguments respectively to sys.argv[1] and sys.argv[2] 

**Sample run in terminal:**
```console
sh runner.sh 4 5
4 or 5 is :  1
```

