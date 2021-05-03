# Semana 2 - Exercícios adicionais (opcionais)
# Exercício 3
# Ana Clara Barbeta

# O programa deve receber um número inteiro e imprimir o dígito das dezenas

numero = int(input("Digite um número inteiro:"))

dezenas = numero // 10
digito = dezenas % 10

print("O dígito das dezenas é", digito)