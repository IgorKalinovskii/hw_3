def slovo():
    while True:
        print('''Введите слово без пробелов в середине слова: \n''')
        x = input()
        # if x.find(' ') == -1:
        if ' ' not in x.strip():
            break
        else:
            print('Таки введите слово без пробелов\n')
            continue

    return x.strip()


print(slovo())
