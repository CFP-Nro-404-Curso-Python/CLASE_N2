'''
CONSIGNAS
=========

1. Creá una variable llamada edad con el valor que quieras.

2. Creá otra variable llamada tiene_entrada que sea un booleano (True o False).

3. Usá un if para verificar las condiciones:
    Si la persona es mayor o igual a 18 años Y tiene entrada, el programa debe imprimir: "¡Bienvenido al evento!".
    Si es mayor de edad pero no tiene entrada, debe decir: "No podés pasar sin entrada".
    En cualquier otro caso (si es menor de edad), debe decir: "Ingreso denegado: Sos menor de edad".

4. Usá un for con range() para generar los números del 3 al 30, pero haciendo que el bucle avance de 3 en 3.
    Dentro del bucle, poné un if para que solo se impriman en pantalla aquellos números que, además de cumplir 
    el salto, sean mayores que 15.
'''

import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. y 2. Variables globales: nombre, edad y tiene_entrada.
nombre = "David Hernán Bravo"
edad = 51
tiene_entrada = True

# Funciones globales.
def permiso_entrada(nombre, edad, tiene_entrada):

    # Usá un if para verificar las condiciones:
    if edad >= 18 and tiene_entrada:
        return f"\n {nombre}, ¡Bienvenido al evento! 🎉\n"
    elif edad >= 18 and not tiene_entrada:
        return f"{nombre}, no podés pasar sin entrada. 🛑\n"
    else:
        return f"{nombre}, ingreso denegado: sos menor de edad. ⛔\n"

def numeros_en_rango():
    # Uso de for con range() para generar los números del 3 al 30, avanzando de 3 en 3.
    for numero in range(3, 31, 3):
        if numero > 15:
            print(numero)

def main():
    print("\n" + "=" * 21)
    print(" PERMISO DE ADMISIÓN ")
    print("=" * 21 + "\n")

    print(permiso_entrada(nombre, edad, tiene_entrada))

    print("\n" + "-" * 50 + "\n")

    print("\n" + "=" * 18)
    print(" NÚMEROS EN RANGO ")
    print("=" * 18 + "\n")

    # No usamos print() aquí porque la función ya se encarga de imprimir los números.
    numeros_en_rango()

# Punto de entrada del script. 
# Esto verifica si el script se está ejecutando directamente y no siendo importado desde otro lado.
if __name__ == "__main__":
    
    main()