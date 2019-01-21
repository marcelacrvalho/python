velocidade = float(input("Quantos km/h? "))

if velocidade > 80:
    print("Sua velocidade é de {:.2f} km/h, e a velocidade permitida é de 80 km/h".format(velocidade))
    multa = (velocidade - 80) * 7
    print("Multa de R$ {:.2f}".format(multa))
