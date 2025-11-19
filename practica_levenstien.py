def distancia_levenshtein(
    patro, text
) -> int:  # la distancia minima de ediciones entre dos palabras
    if len(text) == 0:
        return len(patro)
    llargada_patro = len(patro) + 1
    llargada_text = len(text) + 1
    matriu_distancies = [[0] * llargada_text for x in range(llargada_patro)]
    for i in range(llargada_patro):
        matriu_distancies[i][0] = i
    for j in range(llargada_text):
        matriu_distancies[0][j] = j
    for i in range(1, llargada_patro):
        for j in range(1, llargada_text):
            deletion = matriu_distancies[i - 1][j] + 1
            insercio = matriu_distancies[i][j - 1] + 1
            substitucio = matriu_distancies[i - 1][j - 1]
            if patro[i - 1] != text[j - 1]:
                substitucio += 1
            matriu_distancies[i][j] = min(insercio, deletion, substitucio)
    return matriu_distancies[llargada_patro - 1][llargada_text - 1]


def comparar_frase():
    num_frase: int = int(input("Cuantas frases quieres introducir: "))
    frase_original: str = input("Introduce una frase original: ")

    longitud_frase: list[int] = []
    frases: list[str] = []
    for i in range(num_frase):
        frase: str = input("Introduce una frase: ")
        longitud_frase.append(len(frase))
        frases.append(frase)

    distancias: list[int] = []
    for dis in frases:
        distancia_frase: int = distancia_levenshtein(frase_original, dis)
        distancias.append(distancia_frase)

    espacio: str = max(longitud_frase) * " "
    print(f"Frase {espacio} Distancia")
    for i in range(num_frase):
        print(f"{frases[i]} {espacio} {distancias[i]}")


comparar_frase()
