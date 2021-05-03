# Semana 4 - Exercícios adicionais (opcionais)
# Exercício 2
# Ana Clara Barbeta

# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito 
# com um dígito adjacente igual a ele. Caso exista, imprima "sim". Se não existir, imprima "não"

num = int(input("Digite um numero: "))

anterior = num % 10
num = num // 10
iguais = False
pos = 0

while num > 0 and not iguais:
    atual = num % 10
    if atual == anterior:
        iguais = True
    else:
        pos += 1
    anterior = atual
    num = num // 10

if iguais:
    print("sim")
else:
    print("não")
