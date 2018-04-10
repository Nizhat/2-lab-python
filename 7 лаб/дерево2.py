from sklearn import tree
get = tree.DecisionTreeClassifier()

X = [[1, 1, 0],
     [0, 0, 1],
     [2, 1, 0],
     [1, 0, 0],
     [1, 0, 1],
     [0, 1, 1],
     [2, 0, 1] ]

Y = [0, 1, 1, 1, 1, 0, 1]
get = get.fit(X, Y)


while(True):
    print('')
    ObwPodgotovka = input('Общая подготовка: ')
    slozhnost = input('Сложность экзамена: ')
    podgotovka = input('Готовность к данному предмету: ')
    realData = [[ObwPodgotovka, slozhnost, podgotovka]]

    result = get.predict(realData)
    print(result)
    
