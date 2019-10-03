def inputNum ():
    while True:
        a = input('Введите число:\n')
        try:
            res = int(a)
            break
        except ValueError:
            try:
                res = float(a)
                break
            except ValueError:
                print('Это не число')
                continue
    return res


print(inputNum())
