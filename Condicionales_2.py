## CONDICIONALES ##
# 2. Escriba un programa para encontrar el máximo entre tres números.

num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba un número: "))
num3 = int(input("Escriba un número: "))

max = 0
if num1 == num2 and num2 == num3:
    print("Los tres números ingresados son iguales")
elif num1 >= num2:
    max = num1
    if max >= num3:
        print("El valor máximo es: ",max)
    else:
        print("El valor máximo es: ",num3)
elif num2 >= num1:
    max = num2
    if max >= num3:
        print("El valor máximo es: ",max)
    else:
        print("El valor máximo es: ",num3)
    
