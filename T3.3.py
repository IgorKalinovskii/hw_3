x = int(input('Введите число: '))
counter = 0

if not (x % 2):
    while x % 2 == 0:
        x /= 2
        counter += 1

print('Нацело делили пополам ', counter, ' раз(а)')
