# Semana 4
# Exercício 1
# Ana Clara Barbeta

# Escreva um programa que receba um número n e imprima n! (fatorial)


n = int(input("Digite o valor de n:"))

i = 1
fat = 1

if n == 0:
    print("1")
else:
    while i <= n:
        fat = fat * i
        i += 1
    print(fat)
