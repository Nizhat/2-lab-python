numLength = 10
alphabetLength = 26
n = int(input("Length of password: "))

casesAmount = (numLength + alphabetLength) ** n
print("Количество возможных паролей: %s" % casesAmount)
print("Вероятность взлома пароля с первого раза: %s%%" % (1 / casesAmount * 100))
