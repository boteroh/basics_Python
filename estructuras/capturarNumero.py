valor = input("Ingrese un valor: ")

if valor.isdigit():
    numero = int(valor)
    kelvin = numero + 273.15
    print(f"Los {numero}°C equivalen a {kelvin} K.")

elif valor.replace(".", "", 1).isdigit():
    numero = float(valor)
    if numero > 10.5:
        print(f"El número {numero} es mayor a 10.5.")
    else:
        print(f"El número {numero} no es mayor a 10.5.")

else:
    print("Ingrese su nombre: ")
    nombre = input()
    print(f"Hola, {nombre}!")
