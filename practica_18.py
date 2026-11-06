#GESTOR DE TAREA CON MEMORIA (usando todo lo aprendido)
import ast
def guardar_tareas(nombre_archivo, lista_tareas):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for tarea in lista_tareas:
                archivo.write(f"{tarea}\n")
        print("¡Tarea guardada exitosamente en el archivo!")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
def cargar_tareas(nombre_archivo):
    lista_tarea = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                tarea = ast.literal_eval(linea.strip())
                lista_tarea.append(tarea)
        print("¡Tareas cargadas exitosamente desde el archivo!")
    except FileNotFoundError:
        print("No se encontro un archivo de tarea previo. Iniciando con una lista vacia.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return lista_tarea

nombre = input("¿Cual es tu nombre?: ")
print(f"Hola {nombre} Bienvenido a tu gestor de tareas")

def main():
    # Cargamos las tareas al iniciar el programa
    lista_tareas = cargar_tareas("tareas.txt")
    opcion = ""

    while opcion != 5:
        print("\n--- GESTOR DE TAREAS PENDIENTES ---")
        print("1._ Agregar nueva tarea")
        print("2._ Ver listado de tareas")
        print("3._ Marcar tarea como completada")
        print("4._ Filtrar tareas pendientes")
        print("5._ Salir del sistema")

        try:
            opcion = int(input("Elija una opción (1, 2, 3, 4 o 5): "))

            if opcion == 1:
                print("\n--- AGREGAR NUEVA TAREA ---")
                titulo = input("Ingrese el título de la tarea: ")
                prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
                
                nueva_tarea = {
                    "titulo": titulo,
                    "prioridad": prioridad,
                    "completada": False
                }
                lista_tareas.append(nueva_tarea)
                print(f"¡Tarea '{titulo}' agregada con éxito!")

            elif opcion == 2:
                print("\n--- LISTADO DE TAREAS ---")
                if len(lista_tareas) == 0:
                    print("No hay tareas registradas todavía.")
                else:
                    for indice, tarea in enumerate(lista_tareas, start=1):
                        # Usamos un texto para mostrar si está completada o pendiente
                        estado = "Completada" if tarea["completada"] else "Pendiente"
                        print(f"{indice}. [ ] {tarea['titulo']} - Prioridad: {tarea['prioridad']} - Estado: {estado}")

            elif opcion == 3:
                print("\n--- MARCAR TAREA COMO COMPLETADA ---")
                if len(lista_tareas) == 0:
                    print("No hay tareas para marcar.")
                else:
                    for indice, tarea in enumerate(lista_tareas, start=1):
                        print(f"{indice}. {tarea['titulo']}")
                    
                    num_tarea = int(input("Ingrese el número de la tarea que completó: "))
                    if 1 <= num_tarea <= len(lista_tareas):
                        lista_tareas[num_tarea - 1]["completada"] = True
                        print("¡Excelente! Tarea marcada como completada.")
                    else:
                        print("Número de tarea inválido.")

            elif opcion == 4:
                print("\n--- TAREAS PENDIENTES ---")
                pendientes = [t for t in lista_tareas if not t["completada"]]
                if len(pendientes) == 0:
                    print("¡Felicidades! No tienes tareas pendientes.")
                else:
                    for indice, tarea in enumerate(pendientes, start=1):
                        print(f"{indice}. {tarea['titulo']} (Prioridad: {tarea['prioridad']})")

            elif opcion == 5:
                print("\nSaliendo del sistema...")
                # Guardamos automáticamente antes de cerrar
                guardar_tareas("tareas.txt", lista_tareas)
                print("¡Hasta luego!")

            else:
                print("Opción no válida, ingrese un número del 1 al 5.")

        except ValueError:
            print("¡Inválido! Debes ingresar un número, no letras.")

if __name__ == "__main__":
    main()