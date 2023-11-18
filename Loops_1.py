## LOOPS #
# 1. Escriba un programa para mostrar el patrón como el triángulo de ángulo recto con un asterisco.
#El patrón como:
#*
#**
#***
#****

num = int(input("Ingrese número: "))
ast = ""

for i in range(1,num+1):
    ast = ast + "*"
    i+=1
    print(ast)