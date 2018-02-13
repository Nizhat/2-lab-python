import numpy as np
import matplotlib.pyplot as plt

a = input("Введите строку на английском языке: ")
arr = [0] * 256

for ch in list(a):
    valueOfChar = ord(ch)
    if (valueOfChar >= 97 and valueOfChar <= 122):
        arr[valueOfChar] += 1

x = np.arange(26)
labels = []
for i in range(97, 123):
    labels.append(chr(i))
arr = arr[97 : 123]

fig, ax = plt.subplots()
plt.bar(x, arr)
plt.xticks(x, labels)
plt.show()
