# Semana 7
# Exercício 1
# Ana Clara Barbeta

# Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura de um retângulo;
# O programa deve imprimir uma cadeira de caracteres que represente o retângulo informado com caracteres "#" na saída.
# Dica: a função print pode receber um parâmetro "end", que altera o último caractere da cadeia, tornando possível a remoção
# da quebra de linha.

x = int(input("Digite a largura do retângulo:"))
y = int(input("Digite a altura do retângulo:"))

a = 1

while a <=y :
    print("#" * x, end="")
    print()
    a += 1
