import random

numUser = int(input("Digite um número de 0 a 10: "))

if numUser > 10 or numUser < 0:
    print("Por favor, escreva um número no intervalo de 0 a 10")
else:
    randomico = random.randint(0, 10)
    print("O número escolhido pelo computador foi {} ".format(randomico))
    if randomico == numUser:
        print("Você adivinhou o número do computador!!")
    else:
        print("Você não conseguiu adivinhar o número :(")

