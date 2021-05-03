# Semana 5 - Exercícios adicionais (opcionais)
# Exercício 1 - FizzBuzz
# Ana Clara Barbeta

# Escreva a função FizzBuzz que recebe como parâmetro um número inteiro e devolve:
# - "Fizz" se o número for divisível por 3 e não for divisível por 5;
# - "Buzz" se o número for divisível por 5 e não for divisível por 3;
# - "FizzBuzz" se o número for divisível por 3 e por 5;
# Caso o número não seja divisível por 3 nem por 5, deve devolver o mesmo número recebido como parâmetro.


def fizzbuzz(x):
    if x % 3 == 0 and not x % 5 == 0:
        return "Fizz"
    elif x % 5 == 0 and not x % 3 == 0:
        return "Buzz"
    elif x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    else:
        return x


x = int(input("Digite um número inteiro:"))


print(fizzbuzz(x))