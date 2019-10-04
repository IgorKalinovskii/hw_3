s = '''
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)
'''

print(len(s.split(' ')))

spl = s.split()
print(spl)

newS = []
for el in spl:
    newS.append(el.strip(".!,;:()"))

print(newS)

newS.sort()
print(newS)

d = dict.fromkeys(newS, 0)
for el in newS:
    if el in d:
        d[el] += 1
print(d)

#я понимаю что костыльно и результат не совсем корректный в итоге (титульное написание всех слов-клюей),
#  но, пока не понял как сравнить элемент словаря с другим капитализированным элементом словаря
newCapitalized = []
for el in spl:
    newCapitalized.append(el.capitalize())
print(newCapitalized)

d1 = dict.fromkeys(newCapitalized, 0)
for el in newCapitalized:
    if el in d1:
        d1[el] += 1
print(d1)
