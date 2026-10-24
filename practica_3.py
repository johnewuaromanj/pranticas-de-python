#Calculando presupuesto del dia
nombre = input("¿cual es tu nombre?: ")
print(f"Hola {nombre}, vamos a revisar tus presupuesto de gastos hoy")

presupuesto_diario = float(input("¿Cual es tu presupuesto diario?: "))
pasaje = float(input("¿Cuanto gastaste en pasajes?: "))
comida = float(input("¿Cuanto gastaste en comida?: "))
otros_gastos = float(input("¿Cuanto fueron tus gastos extras?: "))

gasto_total = pasaje + comida + otros_gastos

print("-------------------")
print(f"Los gastos totales de hoy de {nombre}, fueron de: {gasto_total}")

if gasto_total > presupuesto_diario:
    print(f"Cuidado {nombre}, te pasaste de tu limite diario por: {gasto_total - presupuesto_diario}")
else:
    print(f"Excelente {nombre}, estas dentro de tu limite diario")