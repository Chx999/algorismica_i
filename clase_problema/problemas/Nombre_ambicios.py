def perfecte(nre: int) -> bool:
    #    divisors_nre = []  # Genera la lista de divisores de nre(sin incluir el mismo nre)
    #    for divisor in range(1, nre):
    #        if nre % divisor == 0:
    #            divisors_nre.append(divisor)
    divisors_nre = [i for i in range(1, nre) if nre % i == 0]

    suma_divisors = sum(divisors_nre)  # Calcula la suma de los divisores

    if suma_divisors == nre:  # Comprueva si la suma de divosores es igual a nre
        return True
    else:
        return False


def ambicios(num: int) -> bool:
    number_got = [int(1)]
    while num not in number_got:
        number_got.append(num)
        divisor = [i for i in range(1, num) if num % i == 0]
        print(f"Divisores propios de {num} es {divisor}")
        num = sum(divisor)
    print(f"Durante el proceso los numeros conseguidos son {number_got[1:]}")
    return True if perfecte(number_got[-1]) else False


# print(perfecte(100))
print(ambicios(143))
