number = input("Digite o número binário: ")
def binar_para_decima(number):
    if number == "":
        return 0
    else:
        return int(number[0]) * (2 ** (len(number)-1)) + binar_para_decima(number[1:])
resultado_conversao = binar_para_decima(number)
print(f"Número Decimal: {resultado_conversao}")
