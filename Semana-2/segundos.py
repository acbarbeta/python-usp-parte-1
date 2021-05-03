# Semana 2 - Exercícios adicionais (opcionais)
# Exercício 2
# Ana Clara Barbeta

# Escreva um programa que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. 


seg = int(input("Por favor, insira o número de segundos que deseja converter:"))

dia = seg // 86400 #86400 segundos num dia, a função devolve a divisão inteira
resto1 = seg % 86400 #resto da divisão
hora = resto1 // 3600 
resto2 = resto1 % 3600
minuto = resto2 // 60
segundo = resto2 % 60

print(dia, "dias,", hora, "horas,", minuto, "minutos e", segundo, "segundos." )