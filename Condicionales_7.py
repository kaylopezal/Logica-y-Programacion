## CONDICIONALES ##
# 7. Escriba un programa para verificar si un caracter es una letra del alfabeto o no.

letra = str(input("Ingrese un caracter: "))

if ord(letra) in range(65,91): # MAYÚSCULAS
    print(letra, "es una letra del alfabeto")
elif ord(letra) in range(97,123): # MINÚSCULAS
    print(letra, "es una letra del alfabeto")
elif ord(letra) == 209 or ord(letra) == 241: # Ñ, ñ
    print(letra, "es una letra del alfabeto") 
else:
    print(letra, "NO es una letra del alfabeto")