def apocaliptic(num: int) -> bool:
    """
    Aquesta funció comprova si un nombre és apocalíptic.

    Parameters
    ----------
    num: int
        El número

    Returns
    -------
    b: bool
        Si el número és apocalíptic
    """
    num_apocalitic = 2**num
    num_apocalitic_str = str(num_apocalitic)
    if num_apocalitic_str.count("666") != 0:
        return True
    else:
        return False


# convertir el num en un str
# mira si num tiene la secuencia 666
# return el resultat


def llista_apocaliptics(minim: int, maxim: int) -> list[int]:
    """
    Aquesta funció calcula tots els nombres apocalíptics dintre d'un rang.

    Parameters
    ----------
    minim: int
        Cota inferior
    maxim: int
        Cota superior

    Returns
    -------
    llista: list[int]
        Llista amb tots els nombres apocalíptics dintre del rang
    """
    lista_num_apocaliptics = []
    for num in range(minim, maxim):
        if apocaliptic(num):
            lista_num_apocaliptics.append(num)

    return lista_num_apocaliptics


print(apocaliptic(157))
print(llista_apocaliptics(100, 300))
print(len(llista_apocaliptics(0, 5000)))
# Una lista para guardar los num apocalipticos
# Iteracion for del minimo al maximo
# comprueba si el num es apocaliptico
# si lo es lo metemos en la lista
# Retornar la lista
