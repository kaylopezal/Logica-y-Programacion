## LOOPS ##

#5. Escriba un programa para hacer un patrón como un triángulo rectángulo con el número aumentado en 1.
#El patrón como:
#1
#2 3
#4 5 6
#7 8 9 10

num = int(input("Ingrese un número: "))
aux = ""
cont = 0
for i in range(1,num+1):
    for j in range(1,i+1):
        cont = cont + 1
        aux = aux + " " + str(cont)
    print(aux)
    aux = ""
        
        
        