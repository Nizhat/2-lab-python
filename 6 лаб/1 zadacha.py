import numpy as np
import matplotlib.pyplot as plt
arr = []
for i in range(int(input())):
    arr.append(np.random.randint(0,10))
print(arr)
print(arr)

hits = []
for item in arr:
    tally = arr.count(item)
    values = (tally, item)
    if values not in hits:
        hits.append(values)
hits.sort(reverse=True)
if hits[0][0]>hits[1][0]:
    print("\n\nThe mode is:", hits[0][1], "hit appeared", hits[0][0], "times.")
else:
    print("There is not a mode")

def average(list):
    sum = float(0)
    for i in range(len(list)):
        sum += list[i]
    print(sum/len(list))

average(arr)

def median(list):
    n = len(list)
    if n % 2 == 1:
            print(sorted(list)[n//2])
    else:
            print(sum(sorted(list)[n//2-1:n//2+1])/2.0)

median(arr)

dpi = 100
fig = plt.figure(dpi = dpi, figsize = (600 / dpi, 400 / dpi) )


plt.title('Гистограмма')

ax = plt.axes()

xs = range(len(arr))
plt.bar([x + 0.0 for x in xs],  arr,
          color = 'b', alpha = 0.8,
         zorder = 0)
plt.xticks(xs, arr, rotation = 10)
plt.show()
    
      
      
