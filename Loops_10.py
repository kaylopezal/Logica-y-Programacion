## LOOPS ##

# 10. Escriba un programa que dado un número muestre cada uno de sus dígitos, (ejemplo: dado 1567 muestra 1 5 6 7)

num = int(input("Ingrese un número: "))
aux = ""
for i in str(num):
    aux = aux + " " + i
print(aux)