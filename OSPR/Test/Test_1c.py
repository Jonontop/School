"""
(3 točke) Napišite funkcijo vaja_03_c, ki prejme seznam terk in vrne eno terko, ki vsebuje vse 
elemente iz seznama, vendar brez podvojenih elementov.
Primer: unikatna_terka([(1, 2, 3, 4), (3, 4, 5, 6), (5, 6, 7, 8)]) vrne (1, 2, 3, 4, 5, 6, 7, 8)
"""


def vaja_03_c(terke):
def vaja_03_c(terke):
    # Uporabimo seznam za ohranjanje vrstnega reda in set za odstranjevanje podvojenih elementov
    unikatni_elementi = []
    videni = set()
    
    for terka in terke:
        for element in terka:
            if element not in videni:
                unikatni_elementi.append(element)
                videni.add(element)
    
    # Vrne seznam unikatnih elementov kot terko
    return tuple(unikatni_elementi)

# Primer uporabe
print(vaja_03_c([(-1, -2, -3), (1,), (3, 1, 2)]))

print(vaja_03_c([(-1, -2, -3), (1,), (3, 1, 2)]))

def vaja_03_c_test():
    print(f"preverjanje naloge 03, skupina c")
    test_data = [
        [(1, 2, 3, 4), (3, 4, 5, 6), (5, 6, 7, 8)],
        [(1, 1, 1), (1, 1, 1)],
        [(1,), (1,), (1,)],
        [(1,)],
        [(-1, -2, -3), (1, ), (3, 1, 2)]
    ]
    results = [
        (1, 2, 3, 4, 5, 6, 7, 8),
        (1,),
        (1,),
        (1,),
        (1, 2, 3, -2, -3, -1)
    ]

    for i in range(len(test_data)):
        if vaja_03_c(test_data[i]) == results[i]:
            print(f"{i + 1}. primer je OK")

        else:
            print(f"{i + 1}. primer ni OK, vhodni podatki: {test_data[i]}, pričakovan rezultat: [{results[i]}]")

    print()

# vaja_03_c_test()
