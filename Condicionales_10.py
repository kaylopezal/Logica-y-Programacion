## CONDICIONALES ##
# 10. Escriba un programa para verificar
# si un caracter está en mayúsculas o en minúscula.

caracter = str(input("Ingrese un carácter: "))

if ord(caracter) in range(65,91):
    print("El carácter ingresado corresponde a una letra MAYÚSCULA")
elif ord(caracter) in range(97,123):
    print("El carácter ingresado corresponde a una letra MINÚSCULA")
else:
    print("El carácter ingresado NO corresponde a una letra MAYÚSCULA o MINÚSCULA")