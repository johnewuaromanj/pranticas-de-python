#mi primer programa de python: calculadola de gastos diarios

nombre = input ("¿Como te llamas?") 
print (f"hola {nombre} vamos a calcular tus gastos de hoy.")

pasajes = float(input("¿Cuanto gastaste en pasajes hoy?")) 
comida = float(input("¿Cuanto gastaste en comida hoy?"))

total = pasajes + comida

print(f"El gasto total de hoy de: {nombre}, fue: {total}")