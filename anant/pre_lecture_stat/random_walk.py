#sample path--distribution
import numpy as np
N=500
pos=0
lst=[]
for k in range(1,N):
    i=np.random.rand()
    if i>0.5:
        pos+=1
    else:
        pos-=1
    lst.append(pos);

import matplotlib.pyplot as plt
plt.plot(range(1,N),lst)
plt.xlabel("steps")
plt.ylabel("position")