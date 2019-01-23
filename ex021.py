soma = 0

for i in range(0, 501):
    if(i % 2 != 0 and i % 3 == 0):
        soma += i

print("A soma dos número ímpares de 0 a 500 e múltiplos de 3 é: {}".format(soma))
