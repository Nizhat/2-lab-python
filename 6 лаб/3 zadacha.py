import statistics 

import numpy as np 
import matplotlib.pyplot as plt 
N = 1000 
lst = np.random.randn(N) 

print("\nRaw data:", lst) 
lst.sort() 
print("Sorted data:", lst) 


def get_mean(list): 
return float(sum(list)/len(list)) 


def get_median(list): 
median_pos = (len(list)+1)/2 
if median_pos == int(median_pos): 
median_pos = int(median_pos-1) 
return list[median_pos] 
else: 
med_avg = [] 
med_avg.append(list[int(median_pos-1.5)]) 
med_avg.append(list[int(median_pos-.5)]) 
return get_mean(med_avg) 





print("Mean:", get_mean(lst)) 
print("Median:", get_median(lst)) 
print("Mode:",statistics.mode(lst))
