def suma_dividors(num: int) -> int:
    """
    sumar els divisors dels numbres entrats
    """
    suma = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            suma = suma + divisor

    return suma


def amics(num1: int, num2: int) -> bool:
    """
    Aquesta funció comprova si dos nombres són amics.

    Parameters
    ----------
    num1: int
        El primer número
    num2: int
        El segon números

    Returns
    -------
    b: bool
        Si la parella de nombres d'entrada són amics
    """

    suma1 = suma_dividors(num1)
    suma2 = suma_dividors(num2)
    if suma1 == num2 and suma2 == num1:
        return True
    else:
        return False


print(amics(220, 230))
