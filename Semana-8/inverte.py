# Semana 8 - Exercícios adicionais (opcionais)
# Exercício 2 - Invertendo a sequência
# Ana Clara Barbeta

# Escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa.
# A sequência sempre termina pelo número 0.
# Note que o 0 não deve fazer parte da sequência.


n = int(input("Insira um número:"))

lista = []


while n != 0:
    lista.append(n)
    n = int(input("Insira um número:"))
    
lista = lista[::-1]

for i in lista:
    print(i)