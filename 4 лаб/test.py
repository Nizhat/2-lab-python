import numpy as np
import matplotlib.pyplot as plt

a = input("Введите строку на английском языке: ")
arr = [0] * 9

for ch in list(a):
    if (ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8'or ch == '9'):
        valueOfNumber = int(ch)
        arr[valueOfNumber] += 1

print(arr)

'''
x = np.arange(26)
labels = []
for i in range(97, 123):
    labels.append(chr(i))
arr = arr[97 : 123]

fig, ax = plt.subplots()
plt.bar(x, arr)
plt.xticks(x, labels)
plt.show()
'''

