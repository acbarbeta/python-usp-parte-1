# Semana 4
# Exercício 3
# Ana Clara Barbeta

# O programa deve receber um número inteiro, calcular e imprimir a soma dos dígitos desse número


n = int(input("Digite um número inteiro"))


i = 0
while n:
    i = i + n % 10
    n //= 10 
print(i)