
import numpy as np
import matplotlib.pyplot as plt

for i in range(0,1000):
  N=100
  x=0
  X=[]
  Y=[]
    
  for i in range(1,N): 
    rng = np.random.default_rng()
    e=rng.choice([-1,1])
    x+=e
    X.append(i)
    Y.append(x)
  plt.plot(X,Y)
plt.show()

for i in range(0,1000):
  N=100
  x=0
  X=[]
  Y=[]
    
  for i in range(1,N): 
    e=np.random.exponential(10)
    x+=e
    X.append(i)
    Y.append(x)
  plt.plot(X,Y)
plt.show()