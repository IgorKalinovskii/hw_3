a = input('Введите число А\n')
b = input('Введите число Б\n')

try:
    res = float(a) + float(b)
except ValueError:
    res = str(a) + str(b)

print('Результат', res)
print('Тип результата:', type(res))


