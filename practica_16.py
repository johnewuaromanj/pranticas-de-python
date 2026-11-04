#practica 16 usando txt 
def calcular_total_gastos(lista_gasto):
    total = 0
    for gasto in lista_gastos:
        total += gasto["monto"]
    return total

def guardar_datos(nombre_archivo, presupuesto, lista_gastos):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"{presupuesto}\n")
            for gasto in lista_gastos:
                archivo.write(f"{gasto}\n")
        print("¡Datos guardados exitosamente en el archivo!")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

nombre = input("¿Cual es tu nombre?: ")
print(f"Hola {nombre} vamos a calcular tus gastos con historial detallado")

#creamos variables y lista
lista_gastos = []
presupuesto_diario = 0
opcion = ""

#creamos el bucle con (while), agregado lista y append. Lista detallado con (for)
while opcion != 6:
    print("\n---MENU PRINCIPAL---")
    print("1._ Agregar presupuesto")
    print("2._ Agregar gasto actual")
    print("3._ Ver saldo actual")
    print("4._ Ver historial de gastos detallado")
    print("5._ Filtrar gastos altos")
    print("6._ Salir del menu")
    
    try:
  
        opcion = int(input("Elija una opcion: (1. 2. 3. 4. 5. o 6.): "))
        
        if opcion == 1:
            presupuesto_diario = float(input("¿Cual es tu presupuesto diario?: "))
            print("Presupuesto agregado con exito")
            
        elif opcion == 2:
            print("\n--- AGREGAR GASTO DETALLADO ---")
            #pedimos los datos por separados
            monto_ingresado = float(input("Ingrese el monto del gasto: $"))
            descripcion_del_gasto = input("Ingrese la descripcion del gasto: ")
            
            #creamos el diccionario con la informacion
            nuevo_gasto = {"monto": monto_ingresado,"descripcion": descripcion_del_gasto}
            # lo agregamos a nuestra lista de diccionario
            lista_gastos.append(nuevo_gasto)
            print(f"gasto de ${monto_ingresado} en '{descripcion_del_gasto}' agregado con exito.")
            
            
        elif opcion == 3:
            print("\n--- SALDO ACTUAL ---")
            total_de_gasto = calcular_total_gastos(lista_gastos)
            saldo_actual = (presupuesto_diario - total_de_gasto)
            print(f"Tu saldo actual es de: $ {saldo_actual}")
            
        elif opcion == 4:
            print("\n--- REPORTE DETALLADO DE GASTO ---")
            
            if len(lista_gastos) == 0:
                print("No hay gastos registrados todavia.")
            
            else:
                for indice, gasto in enumerate(lista_gastos, start=1):
                    print(f"Gasto {indice}: ${gasto['monto']} - Descripcion: " f"{gasto['descripcion']}")
                total_calculado = calcular_total_gastos(lista_gastos)
                print(f"Total sumado de gasto: ${total_calculado}")
            
        elif opcion == 5:
            print("\n--- FILTRAR GASTOS ALTOS ---")
            monto_limite = float(input("¿A partir de que monto desea buscar sus gastos? $: "))
            print(f"\nGastos mayores o iguales a ${monto_limite}:")
            contador_encotrado = 0
            
            for gasto in lista_gastos:
                if gasto["monto"] >= monto_limite:
                    print(f"Se encontro un gasto de: ${gasto['monto']} - Descripcion: " f"{gasto['descripcion']}")
                    contador_encotrado += 1
                    
            if contador_encotrado == 0:
                print("No hay ningun gasto registrado que supere ese")
            
        elif opcion == 6:
            print(f"\nHasta luego {nombre}. Saliendo del sistema...")
            print("-" * 30)
            print(f"Resumen final para: {nombre}.")
            print(f"Presupuesto inicial: {presupuesto_diario}")
            
            total_final = calcular_total_gastos(lista_gastos)
            saldo_final = presupuesto_diario - total_final
            
            print("-" * 30)
            print(f"Total de gastos realizados: ${total_final}")
            print(f"Saldo final en la billetera: ${saldo_final}")
            print("-" * 30)
            
            guardar_datos("gasto.txt", presupuesto_diario, lista_gastos)
            
            break
            
        else:
            print("opcion no valida, ingrese (1, 2, 3, 4 5 o 6) ")
    
    except ValueError:
        print("¡Invalido! debes ingresar un numero, no letras.")


        