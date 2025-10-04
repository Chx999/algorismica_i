# def suma_digit(num: int) -> int:
#    suma = 0
#    while num != 1:
#        for digit in str(num):
#            print(digit)
#            suma = suma + (int(digit) ** 2)
#            print(suma)
#            if suma == 4:
#                return 0
#            else:
#                num = suma
#    return 1


def felic(num: int) -> bool:
    """
    Aquesta funció comprova si un nombre és feliç.

    Parameters
    ----------
    num: int
        El número

    Returns
    -------
    b: bool
        Si el número és feliç
    """
    """
    1.Usamos un for bucle para obtener la suma de los cualdrados de los digitos
    2.
    """
    a = []
    while num not in a:
        a.append(num)
        num = sum([int(x) ** 2 for x in str(num)])

    return True if num == 1 else False


print(felic(203))
