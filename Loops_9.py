## LOOPS ##

# 9. Escriba un programa que dado un número imprima la suma de sus dígitos

num = int(input("Ingrese un número: "))
suma = 0
for i in str(num):
    suma = suma + int(i)
print("La suma de los digitos del número",num,"es",suma)