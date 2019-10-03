l = [7,18,4,4,119,119,119,53,53,53,53,53,53,53,53,119,119,119,119,119,119,119,0] #там  3 раза подряд 119, потом 8 раз 53 , потом 7 раз 119
i = 0
count = 1
countGlobal = 1

while l[i] != 0:
    if l[i] == l[i+1]:
        count += 1
    else:
        if countGlobal < count:
            countGlobal = count
            count = 1
    i += 1

print(countGlobal)
