#calculadora de gastos con lista (list) y append 
nombre = input("¿Cual es tu nombre?: ")
print(f"Hola {nombre} vamos a calcular tus gastos con historial detallado")

#creamos variables y lista
lista_gastos = []
presupuesto_diario = 0
opcion = ""

#creamos el bucle con (while), agregado lista y append. Lista detallado con (for)
while opcion != "6":
    print("\n---MENU PRINCIPAL---")
    print("1._ Agregar presupuesto")
    print("2._ Agregar gasto actual")
    print("3._ Ver saldo actual")
    print("4._ Ver historial de gastos detallado")
    print("5._ Filtrar gastos altos")
    print("6._ Salir del menu")
  
    
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
        print("\n--- REPORTE DETALLADO DE GASTO ---")
        total_calculado = 0
        
        for indice, gasto in enumerate(lista_gastos, start=1):
            print(f"Gasto {indice}: ${gasto}")
            total_calculado += gasto
        
        print(f"Total sumado de gasto: ${total_calculado}")
        
    elif opcion == "5":
        print("\n--- FILTRAR GASTOS ALTOS ---")
        monto_limite = float(input("¿A partir de que monto desea buscar sus gastos? $: "))
        print(f"\nGastos mayores o iguales a ${monto_limite}:")
        contador_encotrado = 0
        
        for gasto in lista_gastos:
            if gasto >=monto_limite:
                print(f"Se encontro un gasto de: ${gasto}")
                contador_encotrado += 1
                
        if contador_encotrado == 0:
            print("No hay ningun gasto registrado que supere ese")
        
    elif opcion == "6":
        print(f"Hasta luego {nombre}. Saliendo del sistema...")
        
    else:
        print("opcion no valida, ingrese (1, 2, 3, 4 o 5) ")

print("-" * 30)
print(f"El resumen de: {nombre}, es de: ${presupuesto_diario} y sus gastos fueron: ${lista_gastos}")
print("-" * 30)
        
        