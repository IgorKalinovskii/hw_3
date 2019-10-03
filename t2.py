x = input('Введите строку: \n')
if len(x)%2: #нечетная длина строки
    newStr = x[int((len(x)+1)/2):] + x[:int((len(x)+1)/2)]
else:
    newStr = x[int(len(x)/2):] + x[:int(len(x)/2)]
print('Новая строка: ', newStr)
