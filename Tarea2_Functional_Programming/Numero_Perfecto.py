def numero_perfecto(int1):
    es_perfecto = False
    accum = 0
    for divisor in range(1, int1):
        if int1 % divisor == 0:
            accum += divisor

    if accum == int1:
        es_perfecto = True

    return es_perfecto


num = int(input("Digite el numero a evaluar: "))

if numero_perfecto(num) is True:
    print("El numero digitado es un numero perfecto")

else:
    print("El numero digitado NO es un numero perfecto")
