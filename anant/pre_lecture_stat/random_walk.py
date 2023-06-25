#sample path--distribution
import matplotlib.pyplot as plt
import numpy as np
N=50000
pos=0

for j in range(1,50):
    pos=0
    lst=[]
    for k in range(1,N):
        
        i=np.random.rand()
        if i>=0.5:
            pos+=1
        else:
            pos-=1
        lst.append(pos)

    plt.plot(lst)

plt.xlabel("steps")
plt.ylabel("position")
