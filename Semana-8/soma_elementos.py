# Semana 8
# Exercício 2 - Soma dos elementos de uma lista
# Ana Clara Barbeta

# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro
# correspondente à soma dos elementos da lista recebida.



def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma

lista = [2, 4, 2, 2, 3, 3, 1]

print(soma_elementos(lista))