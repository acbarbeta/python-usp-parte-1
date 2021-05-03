# Semana 7 - Exercícios adicionais (opcionais)
# Exercício 2 - Soma das hipotenusas
# Ana Clara Barbeta

# Escrever função soma_hipotenusas que recebe como parâmetro um número inteiro positivo n
# e devolve a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo
# retângulo com catetos inteiros. Lembrete: cada número deve ser somado apenas uma vez.

from math import sqrt


def eh_hipotenusa(hipotenusa):
    # Busca os catetos inteiros, de 1 a n. Se houver ocorrrências, devolve True. Senão, False.
    i = 1

    while i < hipotenusa:
        cat = (hipotenusa ** 2) - (i ** 2)
        if cat > 0:
            cat = sqrt(cat)

            if cat % 1 == 0:
                return True
        
        i += 1
    
    return False


# Agora vamos para a soma. A função soma todos os inteiros entre 1 e n que são comprimento da hipotenusa
# de um triângulo retângulo com catetos inteiros.

def soma_hipotenusas(num):
    hipotenusas = []
    hip = 1

    while hip <= num:
        if eh_hipotenusa(hip):
            hipotenusas.append(hip)
        hip += 1
    
    return sum(hipotenusas)

n = int(input("Insira um número inteiro positivo:"))


print(soma_hipotenusas(n))