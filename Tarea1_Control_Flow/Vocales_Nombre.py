print("Por favor digite 3 nombres")
vocales = "aeiou"
accum1 = 0
accum2 = 0
accum3 = 0

nombre1 = input("\nDigite el primer nombre: ")
nombre2 = input("Digite el segundo nombre: ")
nombre3 = input("Digite el tercer nombre: ")

for caracter in nombre1:
    if caracter in vocales:
        accum1 += 1

print("La cantidad de vocales en el primer nombre es: ", accum1)

for caracter in nombre2:
    if caracter in vocales:
        accum2 += 1

print("La cantidad de vocales en el segundo nombre es: ", accum2)

for caracter in nombre3:
    if caracter in vocales:
        accum3 += 1

print("La cantidad de vocales en el tercer nombre es: ", accum3)