x = 0
sez1 = []
def nal5():
    global x
    x+=1
    return x
def zdruzevanje(niz1, niz2):
    nal5()
    return "".join([(niz1[i]+niz2[i]) for i in range(len(niz1))])

print(zdruzevanje('banana', 'hruška'))

def iskanje_podniza(sez, niz, str:str = ""):
    nal5()
    return any(niz in "".join(i) for i in sez)

print(iskanje_podniza([['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd'], ['p', 'y', 't', 'h', 'o'], ['p', 'r', 'o', 'g', 'r'], ['a', 'm', 'm', 'i', 'n']], 'prog'))

def sosedje(sez, cilj):
    nal5()
    vrstice = len(sez)
    stolpci = len(sez[0])
    rezultat = [[0] * stolpci for _ in range(vrstice)]

    # Definiranje premikov za sosednje elemente (8 smeri)
    premiki = [
        (-1, -1), (-1, 0), (-1, 1),  # zgoraj
        (0, -1),          (0, 1),    # levo in desno
        (1, -1), (1, 0), (1, 1)      # spodaj
    ]

    for i in range(vrstice):
        for j in range(stolpci):
            for dx, dy in premiki:
                x, y = i + dx, j + dy
                if 0 <= x < vrstice and 0 <= y < stolpci and sez[x][y] == cilj:
                    rezultat[i][j] += 1

    return rezultat

# Testni primer
sez = [

    [1, 2, 2, 1],
    [2, 2, 3, 1],
    [1, 3, 3, 2],
    [1, 2, 1, 1]
]
cilj = 2

rezultat = sosedje(sez, cilj)
print(rezultat)


def nal7():
    import random
    global sez1
    sez1.append(random.randint(1, 10))
    return sez1

print(nal7())

def kalkulator(operacija:str, *args:int):
    operacije = ["+", "-", "*", "/"]
    if operacija not in operacije:
        return "Neveljaven operator"

    for i in range(len(args)):
        if operacija == operacije[0]:
            return sum(args)
        elif operacija == operacije[1]:
            y = 0
            for i in args:
                y-=i
            return y
        elif operacija == operacije[2]:
            y = 0
            for i in args:
                y*=i
            return y
        else:
            y = 0
            for i in args:
                y/=i
            return y


print(kalkulator("-", 1,2,3,4))

def vse_vsote(*args):
    vsote = set()
    n = len(args)

    for i in range(n):
        for j in range(i + 1, n):
            vsota = args[i] + args[j]
            vsote.add(vsota)
    return sorted(vsote)

print(vse_vsote(1, 2, 3))

def vaja10(*args):
    listX =[]
    [listX.extend(i) for  i in args]

    return listX

print(vaja10([1, 3, 5], [2, 3, 6], [0, 7, 5]))


def splosci(*args):
    def flatten(element):
        if isinstance(element, list):
            for item in element:
                yield from flatten(item)  # Rekurzivno obdelaj seznam
        elif isinstance(element, (int, float)):  # Preveri, ali je element številka
            yield element

    return list(flatten(args))

# Testni primer
result = splosci(None, '1', [2, 3], 'adsf', [4, [5, 'x', 6]], 7)
print(result)  # [1, 2, 3, 4, 5, 6, 7]


