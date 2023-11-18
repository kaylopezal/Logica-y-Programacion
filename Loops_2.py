## LOOPS ##
#2. Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número.
#El patrón como:
#1
#12
#123
#1234

num = int(input("Ingrese un número: "))
tri = ""

for i in range(1,num+1):
    tri = tri + str(i)
    print(tri)