# Semana 7
# Exercício 2
# Ana Clara Barbeta

# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem
# na borda do retângulo sejam espaços.

x = int(input("Digite a largura do retângulo:"))
y = int(input("Digite a altura do retângulo:"))

a = 1

while a <=y :
    print("#" * x, end="")
    print()
    a += 1
    while a > 1 and a < y:
        print("#" + " " * (x-2) + "#")
        a += 1