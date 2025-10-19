senha_correta = 1234
senha = int(input("Digite sua senha: "))
while senha:
    if senha == senha_correta:
        break
    else: 
        senha = int(input("Senha incorreta, digite ela novamente: "))
print("Acesso Permitido")