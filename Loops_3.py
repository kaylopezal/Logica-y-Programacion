## LOOPS ##
#3. Escriba un programa para hacer un patrón como un triángulo rectángulo con un número que repetirá un número seguido.
#El patrón como:
#1
#22
#333
#4444

num = int(input("Ingrese un número: "))
aux = ""

for i in range(1,num+1):
    aux = i * str(i)
    print(aux)