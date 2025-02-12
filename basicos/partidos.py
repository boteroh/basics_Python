print("-----------------------------------------------")
pg = input("Partidos ganados: ")
pe = input("Partidos empatados: ")
pp = input("Partidos perdidos: ")

print("-----------------------------------------------")

print(f"Puntos por partidos ganados: {int(pg) * 3}")
print(f"Puntos por partidos ganados: {int(pe) * 1}")
print(f"Puntos por partidos perdidos: {0}")

print("-----------------------------------------------")

print(f"Partidos jugados: {int(pg) + int(pe) + int(pp)}")

print("-----------------------------------------------")

Puntos = int(pg) * 3 + int(pe) * 1
print(f"Total Puntos: {Puntos}")