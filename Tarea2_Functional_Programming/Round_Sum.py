
def round_num(int1, base = 10):
    return base * (round(float(int1) / base))

def round_sum(int1, int2, int3):
    return round_num(int1) + round_num(int2) + round_num(int3)

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

print(round_sum(num1, num2, num3), "es la suma de los 3 numeros redondeados a la decena mas cercana")
