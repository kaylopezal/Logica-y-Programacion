## LOOPS ##

#4. Escriba un programa para imprimir el Triángulo de Floyd.
#1
#01
#101
#0101
#10101

num = int(input("Ingrese un número: "))
aux = ""

for i in range(1,num+1):
    if i%2 != 0:
        aux = "1" + aux
        print(aux)
    else:
       aux = "0" + aux
       print(aux)