## CONDICIONALES ##
# 1. Escriba un programa para encontrar el máximo entre dos números.

num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba un número: "))

if num1 == num2:
    print("Los números son iguales")
elif num1 > num2:
        print("El máximo es:", num1)
else:
    print("El máximo es:", num2)