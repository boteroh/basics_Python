contador = 1
numeros = []

print("\n---> INGRESE NÚMEROS ENTEROS <---")

while contador <= 3:

    try:
        numero = int(input(f"\nNúmero: {contador} \n--> "))
        numeros.append(numero)
        contador += 1
    except ValueError:
        print("ERROR !!! ingresa un número entero válido")

print(numeros)

print(f"\n--> El número mayor es: {max(numeros)} --")
print(f"--> El número menor es: {min(numeros)} --")

match numeros[0]:
    # case _ if numeros[0] != numeros[1] and numeros[1] != numeros[2]:
    #     print("\n***todos los números son diferentes")

    case _ if numeros[0] == numeros[1] and numeros[1] == numeros[2] and numeros[0] == numeros[2]:
        print(f"\nTodos los números son iguales")

    case _ if numeros[0] == numeros[1]:
        print(f"\nNúmeros iguales: {numeros[0]} y {numeros[1]}")
    
    case _ if numeros[1] == numeros[2]:
        print(f"\nNúmeros iguales: {numeros[1]} y {numeros[2]}")

    case _ if numeros[0] == numeros[2]:
        print(f"\nNúmeros iguales: {numeros[0]} y {numeros[2]}")
    
    case _:
        print("\n*** No hay números repetidos ***")