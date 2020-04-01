# Тест простоты Миллера—Рабина

from random import randint
from math import gcd

def primeTest(m, k=20): # m - число, проверяемое на простоту, k - кол-во проверок
    s = 0
    t = m - 1
    while t % 2 == 0:
        t //= 2
        s += 1
    # имеем представление n-1 == 2^s * t, где t - нечетное
    for i in range(k): # делаем k - проверок
        a = randint(2, m-1) # случайное число 2<=a<=m-1
        flag = False # является ли a - свидетелем простоты - пока False
        a_t = pow(a, t, m) # a_t = (a^t) mod m
        if (a_t == 1 or a_t == m-1):
            flag = True
            continue
        else:
            for r in range(1, s):
                a_t = pow(a_t, 2, m)
                if (a_t == m - 1):
                    flag = True
                    continue
        if (not flag): # значит ни одно из условий ни разу не выполнилось => a - не свидетель простоты
            return False
    return True