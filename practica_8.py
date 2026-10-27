#Calculadora que resta gasto =  ejecutando todo lo aprendido
nombre = input("¿Cual es tu nombre? ")
print(f"Hola {nombre}, vamos a evaluar tu presupuesto de hoy")

#creamos variables
presupuesto_diario = 0
opcion = ""


while opcion != "4":
    print("\n---MENU PRINCIPAL---")
    print("1. Agregar presupuesto diario")
    print("2. Agregar un gasto")
    print("3. Ver saldo actual")
    print("4. salir del menu")
    
    opcion = input("\nElija una opcion (1 , 2, 3 o 4): ")
    
    if opcion == "1":
        presupuesto_diario = float(input("\n¿Cual es tu presupuesto del dia?: "))
        
    elif opcion == "2":
        gasto_actual = float(input("Ingresa tu gasto: "))
        presupuesto_diario = presupuesto_diario - gasto_actual
        print(f"\nGasto ingresado con exito")
    
    elif opcion == "3":
        print(f"\nTu saldo actual es de: {presupuesto_diario}")
        
    elif opcion == "4":
        print(f"\nHasta luego {nombre} saliendo del sistema...")
        
    else:
        print("\nOpcion no valida, ingrese una opcion correcta (1, 2, 3 o 4)")
        
print("---------------")
print(f"El valance total de: {nombre} es de ${presupuesto_diario} ")
print("---------------")






 