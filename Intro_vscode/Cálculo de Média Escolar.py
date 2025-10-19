notas = 0
calcular_notas = 0
for i in range(3):
    notas = float(input("Digite suas notas: "))
    calcular_notas += notas
media = calcular_notas / 3
if media >= 7.0:
    print("Aprovado.")
elif media >= 5.0 and media < 7.0:
    print("Recuperação.")
else:
    print("Reprovado.")