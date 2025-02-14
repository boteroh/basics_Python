def obtener_tres_numeros_unicos():
    numeros = []
    
    while len(numeros) < 3:
        try:
            numero = int(input(f"Ingrese el número {len(numeros) + 1}: "))

            if numero in numeros:
                print("\nEse número ya fue ingresado. Ingrese un número diferente.")
            else:
                numeros.append(numero)
        except ValueError:
            print("\nEntrada inválida. Ingrese un número válido.")

    return numeros

def encontrar_numero_medio(numeros):
    numeros.sort()
    return numeros[1] 


numeros = obtener_tres_numeros_unicos()

numero_medio = encontrar_numero_medio(numeros)

print(f"El número medio es: {numero_medio}")
