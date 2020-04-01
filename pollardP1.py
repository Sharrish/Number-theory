# p-1 Алгоритм Полларда

from random import randint
from math import gcd, log

def pollardP1(m):
    B = 13
    BASE = [2, 3, 5, 7, 11, 13]
    a = randint(2, m-2)
    d = gcd(a, m)
    if d >= 2:
        return d
    for q in BASE:
        l = int(log(m, 2) / log(q, 2))
        a = pow(a, pow(q, l), m)
    d = gcd(a-1, m)
    if d == 1 or d == m:
        return 1
    else:
        return d