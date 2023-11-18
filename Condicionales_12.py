## CONDICIONALES ##
# 12. Escriba un programa para ingresar ángulos de un triángulo
# y verifique si es válido o no.

# Se asume que los ángulos ingresados estarán en grados

print("Este programa recibe el valor de tres ángulos y determina si corresponde a un triángulo")

ang1 = int(input("Ingrese el valor del ángulo 1: "))
ang2 = int(input("Ingrese el valor del ángulo 2: "))
ang3 = int(input("Ingrese el valor del ángulo 3: "))

if ang1 + ang2 + ang3 == 180:
    print("Los ángulos ingresados corresponden a los de un tríangulo")
else:
    print("Los ángulos ingresados NO corresponden a los de un triángulo")