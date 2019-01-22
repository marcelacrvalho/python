n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 > n2:
    print("{} é maior que {}".format(n1, n2))
    print("Em ordem crescente, fica: {} - {}".format(n2, n1))
else:
    print("{} é maior que {}".format(n2, n1))
    print("Em ordem crescente, fica: {} - {}".format(n1, n2))
