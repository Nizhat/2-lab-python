import random
def fill():
    for j in range(n):
        l = []
        for i in range(m):
            a = random.randint(1,10)
            l.append(a)
            
        matrix.append(l)
    print(matrix)

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
x = int(input("Умножаем на: "))

matrix = []
print(matrix*x)
fill()
