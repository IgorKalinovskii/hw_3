def triangleType(a,b,c):
    if not ((a + b) > c and (a + c) > b and (b + c) > a):
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral triangle'
    elif a == b or a == c or b == c:
        return 'Isosceles triangle'
    else:
        return 'Versatile triangle'


a = int(input('введите число A\n'))
b = int(input('введите число B\n'))
c = int(input('введите число C\n'))

print(triangleType(a,b,c))
