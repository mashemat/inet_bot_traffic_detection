from random import gauss
from numpy import asarray
from numpy import savetxt
import numpy as np
import math

#shift = 10
# abnormal (mean=4+shift, variance=1)
# normal (mean=70, variance=16)
my_mean = 70
my_variance = 16

#shift = 10 #, we need it for abnormal user generation

#random_numbers = [gauss(my_mean, math.sqrt(my_variance)) for i in range(5000000) + shift ]
random_numbers = np.random.normal(my_mean, math.sqrt(my_variance),1999995) #  + shift #, for abnorma users

#print(np.mean(random_numbers))

savetxt('new_normal.csv', random_numbers , delimiter=',')

