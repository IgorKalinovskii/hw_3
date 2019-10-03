def isATriangle(a,b,c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False


a = int(input('введите число A\n')) #Ввод лучше в функции делать или снаружи? В общем случае.
b = int(input('введите число B\n'))
c = int(input('введите число C\n'))

print(isATriangle(a,b,c))
