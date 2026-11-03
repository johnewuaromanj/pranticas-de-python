#practica rapida de try-except 
print("--- PRUEBA RAPIDA DE TRY-EXCEPT ---")

try:
    #le pedimos al usuario un numero
    numero = float(input("Ingrese un numero: "))
    print(f"¡Excelente! ingresaste el numero: {numero}")
    
except ValueError:
    print("¡Invalido! Debes ingresar un numero, no letras.")