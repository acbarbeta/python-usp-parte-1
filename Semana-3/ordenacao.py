# Semana 3
# Exercício 5 - Verificando ordenação
# Ana Clara Barbeta

# Receba 3 números inteiros e imprima "crescente" se eles forem dados em ordem crescente.
# Caso contrário, imprima "não está em ordem crescente"

x = int(input("Digite o primeiro número inteiro:"))
y = int(input("Digite o segundo número inteiro:"))
z = int(input("Digite o terceiro número inteiro:"))

if x < y and y < z:
    print("crescente")
else:
    print("não está em ordem crescente")