#Armando un programa usando todo lo aprendido hasta ahora
nombre = input("¿Cual es tu nombre? ")
print(f"Hola {nombre}, Bienvenido a tu gestor de gastos.")

#creamos las variables
gasto_total = 0
opcion = ""

#creamos el bucle con (while)
while opcion != "3":
    print("\n----Bienvenido al menu principal----")
    print("1. Agregar un gasto")
    print("2. Ver gasto total")
    print("3. Salir del menu") 
    
    opcion = input(f"Eige una opcion: ")
    
    if opcion == "1":
        gasto = float(input("¿Cuanto deseas agregar?: "))
        gasto_total = gasto_total + gasto
        print(f"\ngasto agregado con exito, gasto actual: ${gasto_total}")
        
    elif opcion == "2":
        print(f"\nTu gasto total es de: ${gasto_total}")
        
    elif opcion == "3":
        print(f"\nHasta luego {nombre} saliendo del sistema....")
    
    else:
        print("opcion invalida, por favor ingrese una opcion correcta")
        
print("------------------")
print(f"El resummen total de gasto de: {nombre} es de: ${gasto_total} ")
print("----------------------")
        
        