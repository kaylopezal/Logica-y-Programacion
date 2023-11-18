## CONDICIONALES ##
# 13. Escriba un programa para ingresar todos los lados
# de un triángulo y verifique si es válido o no.

print("El programa recibe tres longitudes, y determina si corresponden a un triángulo")

lado1 = int(input("Ingrese la longitud 1: "))
lado2 = int(input("Ingrese la longitud 2: "))
lado3 = int(input("Ingrese la longitud 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Las longitudes ingresadas corresponden a un TRIÁNGULO")
else:
    print("Las longitudes ingresadas NO corresponden a un TRIÁNGULO")