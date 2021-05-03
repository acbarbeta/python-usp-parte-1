# Semana 3 - Exercícios adicionais (opcionais)
# Exercício 1 - Distância entre dois pontos
# Ana Clara Barbeta

# Receba quatro números, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano.
# Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima "longe". Caso contrário, imprima "perto"


from math import sqrt

x1 = int(input("Insira o primeiro número da coordenada x:"))
y1 = int(input("Insira o primeiro número da coordenada y:"))
x2 = int(input("Insira o segundo número da coordenada x:"))
y2 = int(input("Insira o segundo número da coordenada y:"))


d = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if d >= 10:
    print("longe")
else:
    print("perto")