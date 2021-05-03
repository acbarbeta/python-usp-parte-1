# Semana 3
# Exercício 2 - FizzBuzz parcial - parte 1
# Ana Clara Barbeta

# Receba um número inteiro e imprima Fizz se o número for divisível por 3.
# Caso contrário, imprima o mesmo número que foi dado na entrada.


x = int(input("Digite um número inteiro:"))

if x%3 == 0:
    print("Fizz")
else:
    print(x)