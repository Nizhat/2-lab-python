from sklearn import tree
get = tree.DecisionTreeClassifier()
#рост, длина волос, тембр

X = [[180, 15, 0], [167, 42, 1], [136, 35, 1], [174, 15, 0], [141, 28, 1]]
Y = ['man', 'woman', 'woman', 'man', 'woman']

get = get.fit(X, Y) 
result = get.predict([[133, 37, 1]])
print(result)
