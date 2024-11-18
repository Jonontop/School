def prastevila(n:int) -> list[int]:
    L = [x for x in range(2,n)]
    for i in [2,3,5,7]:
        for j in L:
            if j%i==0 and i!=j:
                L.remove(j)
        return L

# prastevila(30)

def isprime(n:int):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(isprime(12))

def najdaljse_podzaporedje(sez:list[int]) -> None:
    for i in range(1,len(sez)-1):
        if sez[i-1] > sez[i]:
            sez.remove(sez[i])
    print(sez)

# najdaljse_podzaporedje([3,10,2,1,20])

def program1(n1:str, n2:str) -> str:
    for x,y in zip(n1,n2):
        if x == y:
            return "nista ciklična permutacija"

    return "ciklična permutacija"

# program1("abc", "fge")

def Caesarjeva_sifra(niz:str, n:int) -> str:
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

def mediana(sez:list[int]) -> int:
    while len(sez) > 2:
        V = max(sez)
        M = min(sez)
        sez.remove(M)
        sez.remove(V)
    return sez[1] if len(sez) == 2 else sez[0]

# mediana([7, 1, 3, 5, 9, 6] )

def program2(sez:list[list[int]]) -> list[int]:
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

def piramida(n:int):
    x = n+1
    for i in range(-1, n*2, +2):
        x-=1
        print(x*" " + i*"*")

#piramida(5)

def prvo_vecje_prastevilo(n:int) -> int:
    while not isprime(n):
        n+=1
    return n

# print(prvo_vecje_prastevilo(10))

def stevilo_besed(n:str):
    return n.count(" ")+1

# print(stevilo_besed('Python je zabaven'))

def najdaljsa_beseda(n:str):
    x = n.split(" ")
    return max(x, key=lambda x:len(x))

najdaljsa_beseda('Danes je čudovit dan za učenje novih stvari.')

def sorting(sez:list[str]):
    return sorted(sez, reverse=True)

# print(sorting(['banana', 'jabolko', 'kivi'] ))

def odstani_podvojene(sez:list[int]) -> list[int]:
    return list(set(sez))

print(odstani_podvojene([1, 2, 2, 3, 4, 4, 5] ))


# Save the results to a text file
with open("results.txt", "w") as file:
    file.write(f"Prastevila(30): {prastevila(30)}\n")
    file.write(f"Isprime(12): {isprime(12)}\n")
    file.write(f"Najdaljse podzaporedje([3,10,2,1,20]): {najdaljse_podzaporedje([3,10,2,1,20])}\n")
    file.write(f"Program1('abc', 'fge'): {program1('abc', 'fge')}\n")
    file.write(f"Caesarjeva sifra('zza', 3): {Caesarjeva_sifra('zza', 3)}\n")
    file.write(f"Mediana([7, 1, 3, 5, 9, 6]): {mediana([7, 1, 3, 5, 9, 6])}\n")
    file.write(f"Program2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]): {program2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}\n")
    file.write(f"Prvo vecje prastevilo(10): {prvo_vecje_prastevilo(10)}\n")
    file.write(f"Stevilo besed('Python je zabaven'): {stevilo_besed('Python je zabaven')}\n")
    file.write(f"Najdaljsa beseda('Danes je čudovit dan za učenje novih stvari.'): {najdaljsa_beseda('Danes je čudovit dan za učenje novih stvari.')}\n")
    file.write(f"Sorting(['banana', 'jabolko', 'kivi']): {sorting(['banana', 'jabolko', 'kivi'])}\n")
    file.write(f"Odstani podvojene([1, 2, 2, 3, 4, 4, 5]): {odstani_podvojene([1, 2, 2, 3, 4, 4, 5])}\n")
