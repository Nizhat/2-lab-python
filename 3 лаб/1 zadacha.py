import numpy as np

a = [[1, 2, 3],
     [1, 5, 6],
     [7, 8, 9]] 
b = [[3, 1, 7],
     [8, 5, 4],
     [1, 5, 6]]


def printA(): 
    for i in range(len(a)):
        print(a[i])
 
def printB():
    for i in range(len(a)):
        print(b[i])

def umnozhnaChislo(a): 
    for i in range(len(a)): 
        for j in range(len(a)): 
            a[i][j] *= x 


def plus(a,b): 
    for i in range(len(a)): 
        for j in range(len(a)):     
            a[i][j] += b[i][j]

def transpose(a): 
    for i in range(len(a)): 
        for j in range(0,i): 
            tmp = a[i][j] 
            a[i][j]=a[j][i] 
            a[j][i]=tmp 
    return printA(a) 

    

def multiply(m1,m2):
    s=0     #сумма
    t=[]    #временная матрица
    m3=[] # конечная матрица
    if len(m2)!=len(m1[0]):
        print("Матрицы не могут быть перемножены")       
    else:
        r1=len(m1) #количество строк в первой матрице
        c1=len(m1[0]) #Количество столбцов в 1   
        r2=c1           #и строк во 2ой матрице
        c2=len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]           
    return printA(m3)
                

print("\nТранспонирование матрицы а")
transpose(a)
print("\nПервая матрица")
printA()
print("\nВторая матрица")
printB()
x = int(input("\nВедите число, на которую нужно умножить матрицу: "))
print("Матрица, умноженная на число")
umnozhnaChislo(a) 
printA()
print("\nСумма матриц")
plus(a,b)
printA()
print("\nУмножение двух матриц")
multiply(a,b)





