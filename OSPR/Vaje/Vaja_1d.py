# Izpiše faktoriale števil od 1 do n.
def nal01(n:int, strX:list = [], tmp:int = 1):
    for i in range(1, n+1):
        for j in range(1, i+1):
            tmp *= j
        strX.append(tmp)
        tmp = 1
    return strX

# izpiše številsko piramido

def nal02(n:int, x:int = 0):
    for i in range(1, n+1):
        for _ in range(i, i+i):
            x+=1
            print(x, end=" ")
        print()


def smrecica(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i))
    for _ in range(3):
        print(' ' * (n - 1) + '**')

# recica(3)


def pescena_ura(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i))
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i))

# pescena_ura(3)

def nal03(n:int, x:int = 2, listX:list = []):
    def prastevilo(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in range(n):
        if prastevilo(i):
            listX.append(i)

    for i in range(len(listX)//2-2):
        for j in range(i, i+i):
            x+=1
            print(listX[x-1], end=" ")
        print()

# nal03(50)
# 6.	Napišite program, ki izpiše vse možne kombinacije črk za dano besedo. Uporabi ugnezdene zanke za generiranje kombinacij.
def nal4(beseda:str, tmp=""):
    dolzina = len(beseda)
    for i in range(dolzina):
        for j in range(dolzina):
            for k in range(dolzina):
                if i != j and j != k and i != k:
                    print(beseda[i] + beseda[j] + beseda[k])

# nal4("bla")

def nal5(listX=[]):
    while True:
        x = input("Vnesi: ")
        if x.lower() in "konec":
            break
        listX.append(x)

    listX = list(set(listX))
    listX.sort()
    return f"Vnesenih je bilo {len(listX)} besed, od tega je bilo {len(set(listX))} unikatnih, ta števila so {listX}"

# print(nal5())

def nal6(sez = [[1,2, 3], [4, 5, 6], [7, 8, 9]]):
    [[print(sez[j][i], end=" ") for j in range(len(sez[i]))] and print() for i in range(len(sez))]
    """for i in range(len(sez)):
        for j in range(len(sez)):
            print(sez[j][i], end=" ")
        print()
    """

# nal6()

def nal7(Nsez=[]):
    sez = [-1, 0, 1, 2, -1, -4]
    sez.sort()

    """
    for i in range(len(sez)-3):
            for j in range(3):
                if i + sez[j] + sez[j+1] == 0:
                    Nsez.append([i, sez[j], sez[j+1]])
        return Nsez
    """

    return [[i, sez[j], sez[j+1]] for i in range(len(sez)-3) for j in range(3) if i + sez[j] + sez[j+1] == 0]


# print(nal7())

def nal8(sez = ['abc', 'dbc', 'ebc']):
    for i in range(len(sez[0])):
        if sez[0][i] == sez[1][i] == sez[2][i]:
            return f"Vse tri besede imajo na mestu {i+1}. enako črko: {sez[0][i]}."

#print(nal8())



def nal9():
    sez = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(sez)
    for i in range(n):
        sez[i][i], sez[i][n - 1 - i] = sez[i][n - 1 - i], sez[i][i]
    return sez

"""def nal9():
    sez = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return sez[0][::-1] , sez[1] , sez[2][::-1]"""

# print(nal9())

def nal10(n:int):
    sez = [1, 2, 3]

    [print(sez[i], sez[j]) if i != j else None for j in range(len(sez)) for i in range(len(sez))]

    """for i in range(len(sez)):
        for j in range(len(sez)):
            print(sez[i], sez[j]) if i != j else None"""

nal10(2)






