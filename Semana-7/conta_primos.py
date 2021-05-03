# Semana 7 - Exercícios adicionais (opcionais)
# Exercício 1 - Primos

# Escrever função n_primos que recebe um número inteiro maior ou igual a 2 como parâmetro
# e devolve a quantidade de números primos existentes entre 2 e n (incluindo 2 e n)



#O número é primo?
def primo(num):
    divisores = 0

    for div in range (1, num+1):
        if num % div == 0:
            divisores += 1
            if divisores > 2:
                return False
    
    return True

#conta os números primos entre um número inicial e um final
def quantos_primos(inicio, fim):
    primos = 0
    for atual in range(inicio, fim +1):
        if primo(atual):
            primos += 1
    return primos


# função pedida, conta primos entre 2 e número
def n_primos(num):
    return quantos_primos(2, num)


num = int(input("Insira um número inteiro:"))

print(n_primos(num))
