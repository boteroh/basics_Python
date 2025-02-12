sueldos = {'A': 4000, 'B': 3000, 'C': 2000}

sueldos_empleados = []

contador = 1

while contador <= 5:
    print(f"\nEmpleado {contador}:")
    categoria = input("Ingrese la categoría del empleado (A, B o C): ").upper()
    
    while categoria not in sueldos:
        print("Categoría no válida. Intente nuevamente.")
        categoria = input("Ingrese la categoría del empleado (A, B o C): ").upper()
    
    sueldo = sueldos[categoria]
    sueldos_empleados.append(sueldo)
    print(f"Sueldo asignado: ${sueldo}")
    
    contador += 1

print("\nResumen de sueldos:")
for i, sueldo in enumerate(sueldos_empleados, start=1):
    print(f"Empleado {i}: ${sueldo}")