
def validar_nota(nota):
    try:
        nota = int(nota)
        
        if 0 <= nota <= 5:
            if nota > 3:
                return "APROBADO"
            else:
                return "NO APROBADO"
        else:
            return "La nota debe estar entre 0 y 10."
    
    except ValueError:
        return "\nPor favor, ingresa un número válido."

nota = input("Nota del alumno: ")

resultado = validar_nota(nota)

print(resultado)