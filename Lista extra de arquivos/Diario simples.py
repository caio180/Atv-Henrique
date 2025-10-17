frase = input("Como está se sentindo hoje ? ")
with open ("diario.txt", "a") as diario:
    diario.write(frase + "\n")