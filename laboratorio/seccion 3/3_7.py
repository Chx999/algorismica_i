def calculadora():
    entrada: int = 0
    while entrada != "":
        entrada: str = input("Operacion: ")
        if "+" in entrada:
            operacion: list = entrada.split("+")
            print(int(operacion[0]) + int(operacion[-1]))
        elif "-" in entrada:
            operacion: list = entrada.split("-")
            print(int(operacion[0]) - int(operacion[-1]))
        if "*" in entrada:
            operacion: list = entrada.split("*")
            print(int(operacion[0]) * int(operacion[-1]))


calculadora()
