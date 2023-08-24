#def the index compute function
def compute_index(min_x,max_x,min_y,max_y,curr_x,curr_y,gs):
    index=((curr_x-min_x)/gs)+((max_x+gs-min_x)/gs)*((curr_y-min_y)/gs)
    return index


#generate x and y values
import numpy as np
min_x=0
min_y=0
max_x=10
max_y=10
gs=0.5
x=np.arange(0,max_x+gs,gs)
y=np.arange(0,max_y+gs,gs)

#generate the pitcure
import matplotlib.pyplot as plt
plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 10)
for i in range(0,len(x)):
    for j in range(0,len(y)):
     plt.text(x[i], y[j], str(int(compute_index(min_x,max_x,min_y,max_y,x[i],y[j],gs))), color="red")

plt.show()

