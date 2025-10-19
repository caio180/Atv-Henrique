import random
numero_secreto = random.randint(1,100)

while True:
    palpite = int(input("Digite o número que você acha que é o verdadeiro: "))

    if palpite < numero_secreto:
        print("O número é Maior!")
    elif palpite > numero_secreto:
        print("O número é Menor!")
    else:
        break
print(f"Parabéns você acertou, o número correto era {numero_secreto}.")
