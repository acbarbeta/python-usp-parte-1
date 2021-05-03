# Semana 5
# Exercício 3 - Vogais
# Ana Clara Barbeta

# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante



#v = input("Insira uma letra:")

def vogal(v):
    if v in "aeiou" or v in "AEIOU":
        return True
    else:
        return False


#print(vogal(v))