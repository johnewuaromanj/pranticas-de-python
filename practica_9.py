#calculadora de gastos con lista (list) y append
nombre = input("¿Cual es tu nombre?: ")
print(f"Hola {nombre} vamos a calcular tus gastos")

#creamos variables y lista
lista_gastos = []
presupuesto_diario = 0
opcion = ""

#creamos el bucle con (while), agregado lista y append
while opcion != "5":
    print("\n---MENU PRINCIPAL---")
    print("1._ Agregar presupuesto")
    print("2._ Agregar gasto actual")
    print("3._ Ver saldo actual")
    print("4._ Ver historial de gastos")
    print("5._ Salir del menu")
    
    opcion = input("Elija una opcion: (1. 2. 3. 4. o 5.) ")
    
    if opcion == "1":
        presupuesto_diario = float(input("¿Cual es tu presupuesto diario?: "))
        print("Presupuesto agregado con exito")
    elif opcion == "2":
        gasto_actual = float(input("Agrega un gasto: "))
        presupuesto_diario = presupuesto_diario - gasto_actual
        lista_gastos.append(gasto_actual)
        print("Gasto agregado con exito.")
    elif opcion == "3":
        print(f"Tu saldo es de: ${presupuesto_diario}")
    elif opcion == "4":
        print(f"Tus gastos son: {lista_gastos}")
    elif opcion == "5":
        print(f"Hasta luego {nombre}. Saliendo del sistema...")
    else:
        print("opcion no valida, ingrese (1, 2, 3, 4 o 5) ")

print("-------------------")
print(f"El resumen de: {nombre}, es de: ${presupuesto_diario} y sus gastos fueron: ${lista_gastos}")
print("-------------------")
        
        