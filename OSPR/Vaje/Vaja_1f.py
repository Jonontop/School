def uredi_po_dolzini(seznam):
    n = len(seznam)
    # Mehurčkasto urejanje
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(seznam[j]) > len(seznam[j + 1]):
                # Zamenjaj, če je trenutni element daljši od naslednjega
                seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]
    return seznam

# Primer uporabe
rezultat = uredi_po_dolzini(['banana', 'borovnica', 'jabolko', 'kivi'])
print(rezultat)  # ['kivi', 'banana', 'jabolko', 'borovnica']

# 2. Uredi po zadnji črki
def uredi_po_zadnji_crki(seznam):
    n = len(seznam)
    for i in range(1, n):
        key = seznam[i]
        j = i - 1
        while j >= 0 and key[-1] < seznam[j][-1]:
            seznam[j + 1] = seznam[j]
            j -= 1
        seznam[j + 1] = key
    return seznam

# 3. Uredi in filtriraj
def uredi_in_filtriraj(seznam, meja):
    filtriran = [x for x in seznam if x > meja]
    n = len(filtriran)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if filtriran[j] < filtriran[min_idx]:
                min_idx = j
        filtriran[i], filtriran[min_idx] = filtriran[min_idx], filtriran[i]
    return filtriran

# 4. Uredi po max
def uredi_po_max(seznam):
    n = len(seznam)
    for i in range(1, n):
        key = seznam[i]
        j = i - 1
        while j >= 0 and max(key) < max(seznam[j]):
            seznam[j + 1] = seznam[j]
            j -= 1
        seznam[j + 1] = key
    return seznam

# 5. Uredi 2D
def uredi_2D(*seznami):
    urejeni = []
    for seznam in seznami:
        urejeni.append(sorted(seznam))
    return urejeni

# 6. Uredi po povprečju
def uredi_po_povprecju(seznam):
    n = len(seznam)
    for i in range(1, n):
        key = seznam[i]
        j = i - 1
        while j >= 0 and sum(key) / len(key) < sum(seznam[j]) / len(seznam[j]):
            seznam[j + 1] = seznam[j]
            j -= 1
        seznam[j + 1] = key
    return seznam

# 7. Poišči element
def poisci_element(seznam, element):
    levo, desno = 0, len(seznam) - 1
    while levo <= desno:
        sredina = (levo + desno) // 2
        if seznam[sredina] == element:
            return sredina + 1
        elif seznam[sredina] < element:
            desno = sredina - 1
        else:
            levo = sredina + 1
    return -1

# 8. Poišči palindrom
def poisci_palindrome(niz):
    palindromi = []
    n = len(niz)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if niz[i:j] == niz[i:j][::-1]:
                palindromi.append(niz[i:j])
    return palindromi

# 9. Odstrani dvojnik
def odstrani_dvojike(sez):
    pojavitev = set()
    i = 0
    while i < len(sez):
        if sez[i] in pojavitev:
            sez.pop(i)
        else:
            pojavitev.add(sez[i])
            i += 1
    return sez

# 10. Podseznami z vsoto
def podseznami_z_vsoto(seznam, cilj):
    rezultati = []
    n = len(seznam)

    for i in range(n):
        trenutna_seznam = []
        trenutna_vsota = 0
        for j in range(i, n):
            trenutna_vsota += seznam[j]
            trenutna_seznam.append(seznam[j])
            if trenutna_vsota == cilj:
                rezultati.append(trenutna_seznam.copy())
    return rezultati

# 11. Najpogosteješi element
def najpogostejsi_element(seznam):
    from collections import Counter
    števec = Counter(seznam)
    najpogostejsi = min((ele, cnt) for ele, cnt in števec.items() if cnt == max(števec.values()))
    return najpogostejsi[0]

# 12. Najdaljše naraščajoče zaporedje
def najdaljse_zaporeje(seznam):
    n = len(seznam)
    if n == 0:
        return []

    dolzina = [1] * n
    prejsnji = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if seznam[i] > seznam[j] and dolzina[i] < dolzina[j] + 1:
                dolzina[i] = dolzina[j] + 1
                prejsnji[i] = j

    max_dolzina = max(dolzina)
    indeks = dolzina.index(max_dolzina)

    zaporedje = []
    while indeks != -1:
        zaporedje.append(seznam[indeks])
        indeks = prejsnji[indeks]

    return zaporedje[::-1]



# Seznam imen funkcij
function_names = [
    "uredi_po_dolzini",
    "uredi_po_zadnji_crki",
    "uredi_in_filtriraj",
    "uredi_po_max",
    "uredi_2D",
    "uredi_po_povprecju",
    "poisci_element",
    "poisci_palindrome",
    "odstrani_dvojike",
    "podseznami_z_vsoto",
    "najpogostejsi_element",
    "najdaljse_zaporeje"
]

# Zapis v datoteko
with open('imena_funkcij.txt', 'w') as f:
    for name in range(len(function_names)):
        print(function_names[name]()+"\n", file=f)
