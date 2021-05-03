# Semana 5 - Exercícios adicionais (opcionais)
# Exercício 2 - Máximo com 3 parâmetros
# Ana Clara Barbeta

# Reescreva a função "maximo" do outro exercício, que devolve o maior valor dentre dois inteiros recebidos,
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.


#x = int(input("Insira o primeiro número:"))
#y = int(input("Insira o segundo número:"))
#z = int(input("Insira o terceiro número:"))

def maximo(x, y, z):
    max = 0
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
    

#print(maximo(x,y,z))