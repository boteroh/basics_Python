salario = input("Salario empleado: ")
aumento = 0.15

if int(salario) < 300000:
    inc = int(salario) * aumento
    print(f"Aumento: {inc}")
    print(f"Salario devengado; {int(salario) + inc}")
else:
    print(f"Salario devengado: {salario}")