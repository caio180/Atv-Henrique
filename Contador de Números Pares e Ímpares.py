pares = 0
impares = 0
for i in range(10):
    numero = int(input("Digite números: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Números pares: \n {pares} \n Números impares: \n {impares}")