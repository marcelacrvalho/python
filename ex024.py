verificacao = 0

while verificacao != 1:
    sexo = str(input("Qual é o seu sexo? M/F: "))
    if sexo.upper() != "M" and sexo.upper() != "F":
        verificacao = 0
    else:
        verificacao = 1
        print("Obrigado!")
