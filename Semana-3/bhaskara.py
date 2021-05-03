# Semana 3 - Exercícios adicionais (opcionais)
# Exercício 2 - Desafio da videoaula
# Ana Clara Barbeta

# Escreva um programa que calcule as raízes de uma equação de segundo grau


from math import sqrt

a = float(input("Insira o valor de a:"))
b = float(input("Insira o valor de b:"))
c = float(input("Insira o valor de c:"))

delta = ((b ** 2) - (4 * a * c))

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = ((-b + sqrt(delta)) / (2 * a))
    print("a raiz dupla desta equação é {}".format(x))
else:
    x = ((-b + sqrt(delta)) / (2 * a))
    y = ((-b - sqrt(delta)) / (2 * a))
    if x < y:
        print("as raízes da equação são {} e {}".format(x, y))
    else:
        print("as raízes da equação são {} e {}".format(y, x))