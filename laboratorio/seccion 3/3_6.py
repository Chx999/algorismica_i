import math


def nombre_mes_petit_divisible(n):
    mcm = 1
    for i in range(1, n + 1):
        mcm = mcm * i // math.gcd(mcm, i)
    return mcm


print(nombre_mes_petit_divisible(10))
