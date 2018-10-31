
def is_in_range(int1, int2, int3):
    esta_en_rango = False
    if int1 >= int2 and int1 <= int3:
        esta_en_rango = True
    return esta_en_rango

num1 = int(input("Digite el numero a evaluar: "))
min = int(input("Digite el numero minimo del rango: "))
max = int(input("Digite el numero maximo del rango: "))

if is_in_range(num1, min, max) is True:
    print("El numero digitado esta en el rango entre", min, "y", max)

else:
    print("El numero digitado NO esta en el rango entre", min, "y", max)