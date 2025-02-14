num = input("Indique un número positivo o negativo: ")

try:

    num = float(num)

    if int(num) < 0:
        positivo = int(num) * -1
        print(f"Negativo {num} --> Positivo {positivo}")
    else:
        print(f"Num Digitado --> {num}")

except ValueError:
    print("\n--Ingrese un número válido--")