import matplotlib.pyplot as plt
import random as rand

arr = []
explode = (0.1, 0.1)

for i in range(1, 1001):
    a = rand.randint(1, 100)
    if(a >= 30):
        arr.append(0)#Орел
    else:
        arr.append(1)#Решка

labels = ['Орёл', 'Решка']
val = [0] * 2

for i in range(len(arr)):
    if(arr[i] == 0):
        val[0] += 1
    else:
        val[1] += 1

figure1, ax1 = plt.subplots()
ax1.pie(val, labels = labels,
        autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')
plt.show()
