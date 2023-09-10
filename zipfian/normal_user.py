import numpy as np
import matplotlib.pyplot as plt
import math




data=[]
#data_plot=[]

with open('sever_bins.csv','r') as file:
        for item in file:
         k=math.floor(float(item))
         data.append(k)



bins = range(15) 

print(len(bins))

plt.rcParams['font.size'] = 8
plt.rcParams['axes.titlesize'] = 8
plt.rcParams["figure.figsize"] = [5, 3]
plt.rcParams["figure.autolayout"] = True


# Add labels and title

plt.figure(dpi=130,figsize=(4,3))


colors=[(1,0,0),(0.9,0,0.1),(0.8,0,0.2),(0.7,0,0.3),(0.6,0,0.4),(0.5,0,0.5),(0.4,0,0.6),(0.3,0,0.7),(0.2,0,0.8),(0.1,0,0.9),(0,0,1),(0,0,1),(0,0,1),(0,0,1),(0,0,1)]

#plt.bar(bins, data,color =red_rgb, width = 0.4, align='center', label = "Latency")

print('start plotting')
# Plot the histogram

#plt.bar(bins, data,color =('0.0004','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','0.9','0.01','0.02','0.03','0.04','0.05'), width = 0.4, align='center', label = "Latency")

plt.bar(bins, data,color = 'orange', width = 0.4, align='center')

#plt.yticks([1, 2, 3, 4])
plt.xticks([0,1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14])

plt.yscale('log')

#plt.bar(bins, data,color =('0.0004','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','0.9','0.01','0.02','0.03','0.04','0.05'), width = 0.4, align='center', label = "Latency")

plt.xlabel('bins')
plt.ylabel('count')
plt.title(r'Intense bot requests')
plt.savefig('intense.png')
