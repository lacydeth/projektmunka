import random
elemek = []
for i in range(0, 10):
    elemek.append(random.randint(0, 50))
print(elemek)

n = len(elemek)

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if (elemek[i] > elemek[j]):
            ertek = elemek[i]
            elemek[i] = elemek[j]
            elemek[j] = ertek

print(elemek)