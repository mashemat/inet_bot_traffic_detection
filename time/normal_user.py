import numpy as np
import matplotlib.pyplot as plt
import math

data=[]

with open('normal_5M.csv','r') as file:
	for item in file:
         k=math.floor(float(item))
         data.append(k)


plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 10
plt.rcParams["figure.figsize"] = [5, 3]
plt.rcParams["figure.autolayout"] = True


# Add labels and title

plt.figure(dpi=130,figsize=(4,3))

possible_answers = 4

print('start plotting')
# Plot the histogram
count , bins, ignored = plt.hist(data, bins = range(140), density=True, alpha=0.6, color='b',ec="k")
mu, sigma = 70, 4

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         '--',linewidth=1, color='r')

plt.xlabel('value')
plt.ylabel('probability')
plt.title('Normal user request interarival ($\mu=70$, $\sigma=4$)')
plt.savefig('normal_interarival.png')
