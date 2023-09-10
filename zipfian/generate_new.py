import numpy as np
import matplotlib.pyplot as plt
import math
import random

percentage=0.6
DATA_SIZE=5000000
MAX_DATA=2800000

#fname=['bin0','bin1','bin2','bin3','bin4','bin5','bin6','bin7','bin8','bin9','bin10','bin11','bin12','bin13','bin14']
fname=['abin0','abin1','abin2','abin3','abin4','abin5','abin6','abin7','abin8','abin9','abin10','abin11','abin12','abin13','abin14']

data = [[] for _ in range(15)]
bin_percent = []

cnt=0
for fn in fname:
	with open(fn,'r') as file:
		for item in file:
  			data[cnt].append(item)
	cnt=cnt+1


number_of_data = percentage * DATA_SIZE 
with open('anormal_bins.csv','r') as file:
	for item in file:
		bin_percent.append(int(item)/DATA_SIZE)

sum=0
mix=[]
for count in range(15):
	bin_share = bin_percent[count] * number_of_data
	sum=sum+bin_share
	#print(bin_share)
	select = random.sample(data[count], math.floor(bin_share))
	mix = mix + select
print(sum)
print(len(mix))
with open('new_anormal.csv', 'w') as f:
    # using csv.writer method from CSV package
	for item in mix:
        	f.write(item)

