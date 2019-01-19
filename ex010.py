import math
angulo = float(input("Digite o valor do ângulo: "))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tang = math.tan(angulo)
print("Seno de {}º = {:.3f}".format(angulo, seno))
print("Cosseno de {}º = {:.3f}".format(angulo, cosseno))
print("Tangente de {}º = {:.3f}".format(angulo, tang))
