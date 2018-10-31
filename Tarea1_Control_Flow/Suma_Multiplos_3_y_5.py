print("Por favor digite 2 numeros, considere que el segundo numero debe ser mayor por al menos 50 que el primero\n")
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
accum = 0

while numero1 < 0 or numero2 < 0 or (numero2 - numero1 <= 50):
    print("\nLos numeros digitados no son validos")
    print("Por favor digite 2 numeros, considere que el segundo numero debe ser mayor por al menos 50 que el primero\n")
    numero1 = int(input("Digite el primer numero: "))
    numero2 = int(input("Digite el segundo numero: "))

for numero in range(numero1, numero2+1):
    if numero % 3 == 0 and numero % 5 == 0:
        accum += numero

print("La suma de los numeros multiplos de 3 y 5 del rango digitado es: ", accum)
