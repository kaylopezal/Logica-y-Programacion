## CONDICIONALES ##
# 4.Escriba un programa para verificar si un número es divisible o no por 5 y 11.

num1 = int(input("Ingrese un número: "))

if num1 % 5 == 0 and num1 % 11 == 0:
    print("El número ingresado es divisible por 5 y 11")
else:
    print("El número ingresado NO es divisible por 5 y 11")