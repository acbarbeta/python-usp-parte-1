# Semana 8 - Exercícios adicionais (opcionais)
# Exercício 1 - Maior elemento de uma lista
# Ana Clara Barbeta

# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros
# e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):
    maior = 0
    for i in lista:
        if i > maior or maior == 0:
            maior = i
    
    return maior


lista = [-12, -17, -90]

print(maior_elemento(lista))


