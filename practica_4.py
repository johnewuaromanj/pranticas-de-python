#calculadora acumuladora de gastos diarios ilimitados con el bucle (WHILE)
nombre = input("¿Cual es tu nombre? ")
print(f"Hola {nombre}, hoy vamos a sumar todos tus gastos de hoy")

gasto_total = 0

continuar = "si"

while continuar == "si":
    gasto_actual = float(input(f"¿Cuanto gastaste en este rubro?: "))
    gasto_total = gasto_total + gasto_actual
    continuar = input("¿Deseas agregar otro gasto? si/no: ")
    
print(f"El resumen diario de {nombre}")
print(f"El total acumulado de tus gastos del dia de hoy son: {gasto_total}")

