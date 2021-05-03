# Semana 3
# Exercício 4 - FizzBuzz parcial - parte 3
# Ana Clara Barbeta

# Receba um número inteiro na entrada e imprima FizzBuzz na saída se o número for divisível por 3 e por 5. 
# Caso contrário, imprima o mesmo número que foi dado na entrada



x = int(input("Digite um número inteiro:"))

if x%3 == 0 and x%5 == 0:
    print("FizzBuzz")
else:
    print(x)
