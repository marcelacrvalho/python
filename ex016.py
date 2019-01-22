id = int(input("Qual é a sua idade? "))

if id > 18:
    tempo = id - 18
    print("Passaram-se {} anos para se alistar".format(tempo))
elif id < 18:
    tempo = 18 - id
    print("Faltam {} anos para se alistar".format(tempo))
else:
    print("Você precisa se alistar esse ano!")
