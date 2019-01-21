distancia = float(input("Qual é a distância da viagem em kms? "))

if distancia <= 200:
    valorPassagem = distancia * 0.50
    print("O valor da passagem será de R$ {:.2f}".format(valorPassagem))
else:
    valorPassagem = distancia * 0.45
    print("O valor da passagem será de R$ {:.2f".format(valorPassagem))
