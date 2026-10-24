#calculadora de gastos diarios
nombre = input(f"¿cual es tu nombre?: ")
print(f"Hola {nombre}, vamos a calcular tus gastos de hoy")

pasajes = float(input(f"¿cuanto gastaste en pasajes?: "))
comida = float(input(f"¿cuanto gastaste en comida?: "))
otros_gastos = float(input(f"¿cuanto gastaste en otra cosa extra?: "))

gasto_total = pasajes + comida + otros_gastos

print("-----------------")
print(f"Los gastos de hoy de {nombre}, fueron de: {gasto_total} ")