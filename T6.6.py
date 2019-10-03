def distance(x1, y1,x2,y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**0.5

x1 = float(input('введите x1\n'))
y1 = float(input('введите y1\n'))
x2 = float(input('введите x2\n'))
y2 = float(input('введите y2\n'))

print('Расстояние между двумя точками:', distance(x1,y1,x2,y2))
