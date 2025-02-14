sueldos = {'A': 4000, 'B': 3000, 'C': 2000}

sueldos_empleados = []

try:
    cant_empleados = int(input("\nIngresa la cantidad de empleados: "))
    if cant_empleados <= 0:
        print("\nCantidad de empleados debe ser mayor a cero")
    
    else:
        contador = 1
        while contador <= cant_empleados:
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
except ValueError:
    print("\nPor favor ingrese un número válido para la cantidad de empleados")

contador = 1
