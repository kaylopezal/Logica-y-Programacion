## LOOPS ##
# 6. Escriba un programa que dado un número indique si es primo o no

num = int(input("Ingrese un número: "))
cont = 0
for i in range(1,num//2,2):
    if num%i == 0 and i != 1:
        cont = cont + 1
        if cont > 1:
            print("El número ingresado es NO PRIMO")
    else:
        print("El número ingresado es PRIMO")