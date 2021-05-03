# Semana 3
# Exercício 3 - FizzBuzz parcial - parte 2
# Ana Clara Barbeta

# Receba um número inteiro e imprima Buzz se o número for divisível por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

x = int(input("Digite um número inteiro:"))

if x%5 == 0:
    print("Buzz")
else:
    print(x)