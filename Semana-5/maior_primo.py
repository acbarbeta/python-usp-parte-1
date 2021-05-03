# Semana 5
# Exercício 2 - Primos
# Ana Clara Barbeta

# Escreva a função maior_primo que recebe um número maior ou igual a 2 como parâmetro
# e devolve o maior número primo menor ou igual ao número passado na função


#n = int(input("Insira um número inteiro:"))


def e_primo(num): 
    return all(num%i!=0 for i in range(2,num)) 



def maior_primo(n):
    for num in reversed(range(1,n+1)):
        if e_primo(num):
            return num




#print(maior_primo(n))
