## CONDICIONALES ##
# 6. Escriba un programa para verificar si un año es un año bisiesto o no.

anio = int(input("Ingrese un año de 4 digitos: "))

if anio % 4 == 0:
    print("El año",anio, "es bisiesto")
else:
    print("El año",anio, "NO es bisiesto")
    