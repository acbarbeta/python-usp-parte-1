# Semana 4 - Exercícios adicionais (opcionais)
# Exercício 1
# Ana Clara Barbeta

# O programa deve receber um número inteiro positivo e verificar se é primo. Se for primo, imprima "primo". Caso contrário, "não primo"


def primo(num):
    divisores = 0

    for div in range (1, num+1):
        if num % div == 0:
            divisores += 1
            if divisores > 2:
                return False
    
    return True


num = int(input("Insira um número:"))
if primo(num):
    print("primo")
else:
    print("não primo")
