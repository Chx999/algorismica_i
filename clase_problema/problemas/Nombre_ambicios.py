def perfecte(nre: int) -> bool:
    divisors_nre = []  # Genera la lista de divisores de nre
    for divisor in range(1, nre):
        if nre % divisor == 0:
            divisors_nre.append(divisor)
    print(divisors_nre)

    suma_divisors = 0  # Calcula la suma de los divisores
    for suma in divisors_nre:
        suma_divisors = suma_divisors + suma

    if suma_divisors == nre:  # Comprueva si la suma de divosores es igual a nre
        return True
    else:
        return False


def ambicios(num: int) -> bool:
    pass


print(perfecte(25))
