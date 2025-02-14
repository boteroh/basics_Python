salario = input("Salario empleado: ")

try:
    salario = float(salario)

    if salario < 0:
        print("\nSalario no puede ser negativo")
    else:
        aumento = 0.15

        if salario < 300000:
            inc = salario * aumento
            print(f"Aumento: {inc}")
            print(f"Salario devengado: {salario + inc}")
        else:
            print(f"Salario devengado: {salario}")

except ValueError:
    print("\nPor favor ingrese un número váido")
