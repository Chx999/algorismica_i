def suma_digit(num: int) -> int:
#    while num != 1:
#        for digit in str(num):
#            suma = int(digit) ** 2
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
    if suma_digit(num) == 1:
        return True
    else:
        return False


print(felic(203))
