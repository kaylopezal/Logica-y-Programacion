## CONDICIONALES ##
# 3. Escriba un programa para verificar si un número es negativo, positivo o cero.

num1 = int(input("Ingrese un número: "))

if num1 == 0:
    print("El número es cero")
elif num1 > 0:
    print("El número es positivo")
else:
    print("El número es negativo")