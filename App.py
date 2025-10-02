import random

Pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

statistik_dict = {zahl: 0 for zahl in Pool}

def lottozahlen():
    zPool = Pool.copy()
    gezogene = []
    for i in range(6):

        index = random.randint(0, len(zPool)- 1)
        gezogeneZahl = zPool.pop(index)  # Entfernt an Position index
        gezogene.append(gezogeneZahl)  # Hängt ans Ende an

    return gezogene

zahler = 0;
for i in range(6):
    while zahler <1000:
        ziehung = lottozahlen()
        zahler += 1
        for zahl in ziehung:
            statistik_dict[zahl] += 1

print(statistik_dict)
print(ziehung)














