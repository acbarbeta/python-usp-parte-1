# Semana 2 - Exercícios adicionais (oopcionais)
# Exercício 1
# Ana Clara Barbeta

# Uma empresa de cartão de crédito envia suas faturas por email com uma mensagem.
# Escreva um programa que receba o nome do cliente, o dia e o mês de vencimento e o valor da fatura
# e imprima a mensagem com os dados recebidos. A mensagem é impressa em duas linhas diferentes. 

nome = input("Digite o nome do cliente:")
dia = input("Digite o dia de vencimento:")
mes = input("Digite o mês de vencimento:")
valor = input("Digite o valor da fatura:")

print("Olá,", nome)
print("A sua fatura com vencimento em", dia, "de", mes, "no valor de R$", valor, "está fechada.")