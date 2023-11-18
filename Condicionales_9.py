## CONDICIONALES ##
# 9. Escriba un programa para ingresar a cualquier caracter
# y verificar si es una letra, dígito o carácter especial.

caracter = str(input("Ingrese un carácter: "))

if ord(caracter) in range(65,91) or ord(caracter) in range(97,123):
    print("El carácter ingresado corresponde a una LETRA")
elif ord(caracter) == 209 or ord(caracter) == 241:
    print("El carácter ingresado corresponde a una LETRA")
elif ord(caracter) in range(48,58):
    print("El carácter ingresado corresponde a un DÍGITO")
elif ord(caracter) in range(32,48):
    print("El carácter ingresado corresponde a un CARÁCTER ESPECIAL")
elif ord(caracter) in range(58,65):
    print("El carácter ingresado corresponde a un CARÁCTER ESPECIAL")
elif ord(caracter) in range(91,97):
    print("El carácter ingresado corresponde a un CARÁCTER ESPECIAL")
elif ord(caracter) in range(123,127):
    print("El carácter ingresado corresponde a un CARÁCTER ESPECIAL")
else:
    print("El carácter ingresado corresponde NO es LETRA, DÍGITO o CARÁCTER ESPECIAL")
    

# (32–47 / 58–64 / 91–96 / 123–126)