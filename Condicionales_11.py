## CONDICIONALES ##
# 11. Escriba un programa para que dado el número del mes,
# indique el número de días del mes

mes = int(input("Ingrese el número del mes: "))

if mes in range(1,13):
    if mes == 1:
        print("El mes",mes,"tiene 31 días")
    elif mes == 2:
        print("El mes",mes,"tiene 29 días si es bisiesto, de lo contrario 28 días")
    elif mes == 3:
        print("El mes",mes,"tiene 31 días")
    elif mes == 4:
        print("El mes",mes,"tiene 30 días")
    elif mes == 5:
        print("El mes",mes,"tiene 31 días")
    elif mes == 6:
        print("El mes",mes,"tiene 30 días")
    elif mes == 7:
        print("El mes",mes,"tiene 31 días")
    elif mes == 8:
        print("El mes",mes,"tiene 31 días")
    elif mes == 9:
        print("El mes",mes,"tiene 30 días")
    elif mes == 10:
        print("El mes",mes,"tiene 31 días")
    elif mes == 11:
        print("El mes",mes,"tiene 30 días")
    else:
        print("El mes",mes,"tiene 31 días")
else:
    print("El número ingresado no corresponde a un mes válido")