import random as rand
import numpy as np

print("Задание 1.\n")
a = np.random.random((3,3,3))
print(a)
print("\n*****************************************\n")

print("Задание 2.\n")
n = int(input("Введите размерность массива: "))
a = np.ones((n,n))
a[1:-1,1:-1] = 0
print(a)
print("\n*****************************************\n")

print("Задание 3.\n")
a = np.arange(15)
print(a)
print("\n")
a[(3 < a) & (a <= 10)] *= -1

print(a)
print("\n*****************************************\n")


print("Задание 4.\n")
n = int(input("Размерность массива: "))
p = int(input("Введите число, которое нужно вставить в массив: "))
a = np.zeros((n,n))
np.put(a, np.random.choice(range(n*n), p, replace=False), 1)
print(a)
print("\n*****************************************\n")


print("Задание 5.\n")
c = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(c-v)).argmin()
print(v)
print(c[index])
print("\n*****************************************\n")



print("Задание 6.\n")
b = np.random.randint(1,10,(4, 4))
c = b - b.mean(axis=1, keepdims=True)
print(b)
print(c)
print("\n*****************************************\n")


print("Задание 7.\n")
b = np.random.randint(1,10,(5,5))
print(b)
print("\n*****************************************\n")


print("Задание 8.\n")
h = np.random.randint(0,10,(3,3))
print(h)
rank = np.linalg.matrix_rank(h)
print(rank)
print("\n*****************************************\n")


print("Задание 9.\n")
a = np.random.randint(0,10,50)
print(a)
print(np.bincount(a).argmax())
print("\n*****************************************\n")


print("Задание 10.\n")
Z = np.random.randint(0,10,(10))
print(Z)
Z[Z.argmax()] = 0
print(Z)
