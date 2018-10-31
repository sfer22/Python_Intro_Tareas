
def numero_mayor(int1, int2, int3):
    if int1 > int2 and int1 > int3:
        mayor = int1
    elif int2 > int1 and int2 > int3:
        mayor = int2
    else:
        mayor = int3
    return mayor


num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

print(numero_mayor(num1, num2, num3), "es el numero mayor")
