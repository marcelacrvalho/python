import random

tentativas = 0
pontoParada = 0

while pontoParada != 1:
    numeroEscolhido = int(input("Escolha um número de 0 a 10: "))
    numeroComputador = random.randint(0, 10)
    print("Número escolhido pelo computador - ({})".format(numeroComputador))
    if numeroEscolhido != numeroComputador:
        tentativas += 1
        parador = 0
    else:
        print("Você acertou!!")
        print("Número de tentativas - ({}) ".format(tentativas))
        pontoParada = 1
