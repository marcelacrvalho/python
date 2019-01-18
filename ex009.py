h = float(input("Qual é a altura da parede a ser pintada? "))
l = float(input("Qual é a largura da parede a ser pintada? "))
area = h * l
print("A área total da parede é de {:.2f} m²".format(area))
litros = area/2
print("A quantidade de tinta necessária, será de {:.2f} litros".format(litros))
