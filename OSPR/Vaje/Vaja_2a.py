def vaja1(sez: tuple) -> int:
    return sez[1][1]


print(vaja1(('Jabolko', [10, 20, 30], (5, 15, 25))))


def vaja2(sez: tuple) -> tuple:
    sez = list(sez)
    sez[0], sez[-1] = sez[-1], sez[0]
    return tuple(sez)


print(vaja2((1, 2, 3, 4, 5)))


def vaja3(t1: tuple, t2: tuple) -> tuple:
    return tuple(list(t1 + t2))


print(vaja3((1, 2, 3), (4, 5, 6)))


def vaja4(t1: tuple) -> tuple:
    return tuple(list(sorted(t1, key=lambda x: x[1])))


print(vaja4((('a', 23), ('b', 37), ('c', 11), ('d', 29))))


def vaja5(t1: tuple):
    return max(t1), min(t1)


print(vaja5((4, 7, 1, 9, 2)))


def vaja6(t1: tuple, t2: tuple) -> tuple:
    t1 = set(t1)
    t2 = set(t2)
    return tuple(t1 & t2)


def vaja7(t1: tuple, n: int):
    for i in t1:
        if sum(i) >= n:
            return i


print(vaja7([(1, 2, 3), (4, 5, 6), (1, 1, 1)], 10))


def vaja8(seznam, razlika):
    pare = []
    n = len(seznam)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(seznam[i] - seznam[j]) == razlika:
                pare.append((min(seznam[i], seznam[j]), max(seznam[i], seznam[j])))

    return pare


print(vaja8([1, 5, 3, 4, 2], 2))


def vaja9(t1, t2):
    tmp = []
    for i, j in zip(t1, t2):
        sez = []
        sez.append(i)
        sez.append(j)
        tmp.append(sez)
    return tmp


print(vaja9([1, 2, 3], ['a', 'b', 'c']))


def vaja10(t1):
    tmp = []
    for i in t1:
        if i.isnumeric():
            tmp.append(int(i))
    return tmp


print(vaja10('abc123xyz456'))


def vaja11(t1):
    return max(t1, key=lambda x: t1.count(x))


print((vaja11(((1, 2), (2, 3), (1, 2), (2, 3), (1, 2)))))

def kartezicni_produkt(*terke):
    if not terke:
        return []
    rezultat = []
    def generiraj_product(terke, trenutni):
        if not terke:
            rezultat.append(trenutni)
            return
        for el in terke[0]:
            generiraj_product(terke[1:], trenutni + (el,))
    generiraj_product(terke, ())
    return rezultat

print(kartezicni_produkt((1, 2), (3, 4)) )
