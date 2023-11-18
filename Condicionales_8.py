## CONDICIONALES ##
# 8. Escriba un programa para ingresar cualquier caracter y verifique si es vocal o consonante.

letra = str(input("Ingrese un caracter: "))

if ord(letra) in range(65,91) or ord(letra) in range(97,123):
    if ord(letra) == 65 or ord(letra) == 97: # A, a
        print("El caracter ingresado es una VOCAL")
    elif ord(letra) == 69 or ord(letra) == 101: # E, e
        print("El caracter ingresado es una VOCAL")
    elif ord(letra) == 73 or ord(letra) == 105: # I, i
        print("El caracter ingresado es una VOCAL")
    elif ord(letra) == 79 or ord(letra) == 111: # O, o
        print("El caracter ingresado es una VOCAL")
    elif ord(letra) == 85 or ord(letra) == 117: # U, u
        print("El caracter ingresado es una VOCAL")
    elif rd(letra) == 209 or ord(letra) == 241: # Ñ, ñ
        print("El caracter ingresado es una CONSONANTE") 
    else:
        print("El caracter ingresado es una CONSONANTE")
else:
    print("El caracter ingresado NO es una VOCAL, ni CONSONANTE")