#calculadora con menu interactivo
nombre = input("¿Cual es tu nombre? ")
print(f"Hola {nombre}, bienvenido a tu gestor de finanzas:")

gasto_total = 0
opcion = ""

#el bucle se repite mientras el usuario no elija salir
while opcion != "3":
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar un gasto")
    print("2. Ver total acumulado")
    print("3. Salir del menú")
    
    opcion = input("Elige una opción (1 ,2 o 3): ")
    
    if opcion == "1":
        gasto = float(input("¿Cuanto deseas agregar?: "))
        gasto_total = gasto_total + gasto
        print(f"¡Gasto agregado con exito! Total actual: {gasto_total}")
        
    elif opcion == "2":
        print(f"El total de tus gastos acumulados de hoy es de: {gasto_total}")
        
    elif opcion == "3":
        print(f"¡Hasta luego {nombre}! Cerrando el sistema...")
        
    else:
        print("Opcion no valida, por favor elegir 1, 2 o 3. ")
        
print("---------------------")
print(f"Resumen final del dia de: {nombre}: ${gasto_total}")
print("---------------------")