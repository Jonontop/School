def prastevila(n):
    L = [x for x in range(2,n)]
    for i in [2,3,5,7]:
        for j in L:
            if j%i==0 and i!=j:
                L.remove(j)
        return L

# prastevila(30)

def najdaljse_podzaporedje(sez):
    for i in range(1,len(sez)-1):
        if sez[i-1] > sez[i]:
            sez.remove(sez[i])
    print(sez)

# najdaljse_podzaporedje([3,10,2,1,20])

def program1(n1, n2):
    for x,y in zip(n1,n2):
        if x == y:
            return "nista ciklična permutacija"

    return "ciklična permutacija"

# program1("abc", "fge")

def Caesarjeva_sifra(niz, n):
    Nniz = ""
    abeceda = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z'
    ]
    for i in niz.upper():
        Nniz += (abeceda[(abeceda.index(i))+n])
    return Nniz

# Caesarjeva_sifra("zza", 3)

def mediana(sez):
    while len(sez) > 2:
        V = max(sez)
        M = min(sez)
        sez.remove(M)
        sez.remove(V)
    return sez[1] if len(sez) == 2 else sez[0]

# mediana([7, 1, 3, 5, 9, 6] )

def program2(sez):
    Nsez = []
    for i in sez[0]:
        Nsez.append(i)
    for i in range(1, len(sez)):
        Nsez.append(sez[i][-1])
    for i in range(len(sez[-1])-2, -1, -1):
        print(i)
        Nsez.append(sez[-1][i])
    for i in range(len(sez[-2])-1):
        Nsez.append(sez[-2][i])


    return Nsez


# program2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def piramida(n):
    x = n+1
    for i in range(-1, n*2, +2):
        x-=1
        print(x*" " + i*"*")

piramida(5)
