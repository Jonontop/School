import random
from typing import Union
import time

# 1. Napiši funkcijo, ki vrne seznam števil od 1 do n
napolni = lambda n: [i for i in range(1, n+1)]
# print(napolni(1000)) 

# 2. Napiši funkcijo, ki vrne seznam n naključnih števil
my_list = lambda :[random.randint(1, 100) for _ in range(20_000)]
my_list = napolni(20_000)

# 3. Napiši funkcijo, ki vrne seznam n naključnih števil, ki so urejeni
my_list.sort()

# 4. Napiši funkcijo, ki vrne seznam n naključnih števil, ki so urejeni padajoče
my_tuple = tuple(my_list.copy())

# 5. Napiši funkcijo, ki vrne True, če je iskano število v seznamu, sicer False
def linearno_iskanje(iterable:Union[tuple,list], iskano: int) -> int:
    iterable = list(iterable) if isinstance(iterable,tuple) else iterable
    for i in range(len(iterable)):
        if iterable[i] == iskano:
            return i
    return -1




rez = 0
# 6. Napiši funkcijo, ki vrne index, če je iskano število v seznamu s pomočjo binarnega iskanja, sicer -1
def binarno_iskanje(iterable:Union[tuple,list], iskano: int) -> int:
    iterable = list(iterable) if isinstance(iterable,tuple) else iterable
    start = 0
    end = len(iterable) - 1
    while start <= end:
        mid = (start + end) // 2
        if iterable[mid] == iskano:
            return mid
        elif iterable[mid] < iskano:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Testiranje
n = 1_000_000
start = time.time()
for i in range(n):
    rez = linearno_iskanje(my_list, 5) # True
print(time.time() - start)

start = time.time()
for i in range(n):
    binarno_iskanje(my_list, 5) # True
print(time.time() - start)

start = time.time()
for i in range(n):
    rez = my_list.index(5) # True
print(time.time() - start)

