x=input('Введите строку \n')
try:
    print(
    x[2],
    x[-2],
    x[0:5],
    x[:-2],
    x[::2],
    x[1::2],
    x[::-1],
    x[::-2],
    x[-2::-2],
    x[-2:0:-1],
    len(x),
    sep="\n"
    )
except IndexError as e:
    print(e)