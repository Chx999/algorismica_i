def districte_barri() -> dict[str, str]:
    """
    Retorna un diccionari amb els districtes i barris de Barcelona.

    La clau del diccionari és el nom del barri i el valor és el nom del districte.

    :param: None
    :return: diccionari amb els barris de Barcelona i el seu districte corresponent.
    """
    # Inicialitzar un diccionari buit
    # Obrir el archivo
    # Bucle per Llegir el archivo en linia a linia
    # far el districte i el barri
    # Mirar si el barri esta al diccionari
    # Si no hi es afegir el barri i el districte al diccionari
    # Retornar el diccionari
    districto = {}
    archivo = open("sense_comes_renda_reduit.csv", "r")
    for line in archivo:
        contenido = line.split(";")
        districto[contenido[4]] = contenido[2]
    print(districto)
    archivo.close()


districte_barri()
