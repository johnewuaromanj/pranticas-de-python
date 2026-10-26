#calculadora acumuladora de gastos diarios ilimitados con el bucle (WHILE)
nombre = input("¿Cual es tu nombre? ")
print(f"Hola {nombre}, vamos a sumar todos tus gastos de hoy")

gasto_total = 0

gasto_inicial = float(input("¿Cual fue tu primer gasto del dia?: "))
gasto_total = gasto_total + gasto_inicial

continuar = input("¿Quieres agregar otro gasto? si/no: ").lower()

while continuar == "si":
    gasto_siguiente = float(input(f"¿Cual fue tu siguiente gasto?: "))
    gasto_total = gasto_total + gasto_siguiente
    continuar = input("¿Deseas agregar otro gasto? si/no: ").lower()
    
print(f"El resumen diario de {nombre}")
print(f"El total acumulado de tus gastos del dia de hoy son: {gasto_total}")