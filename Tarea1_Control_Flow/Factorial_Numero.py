numero = int(input("Digite un numero entre 0 y 30: "))
factorial = 1

while numero < 0 or numero > 30:
    print("\nERROR, revise su seleccion de numeros!!!!\n")
    numero = int(input("Digite un numero entre 0 y 30: "))

for factor in range(1, numero+1):
    factorial = factorial * factor

print("El factorial del numero", numero, "es: ", factorial)