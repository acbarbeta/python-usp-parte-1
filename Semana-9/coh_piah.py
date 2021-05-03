# Semana 9
# Programa completo - Similaridades entre textos - Caso COH-PIAH
# Ana Clara Barbeta

import re

def le_assinatura():
    #A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura para comparação com o fornecido
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    #Lê os textos a serem comparados, que são devolvidos como elemento de lista
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    #Lê um texto e devolve uma lista com os preíodos
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #Lê o período e separa as frases como elementos de uma lista
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #Lê a frase e separa as palavras como elemento de lista
    return frase.split()

def n_palavras_unicas(lista_palavras):
    #Quais palavras da lista aparecem uma única vez?
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    #Quantas palavras diferentes foram utilizadas?
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    soma = 0
    for i in range(len(as_a)):
        soma = soma + abs(as_a[i] - as_b[i])
    return soma / 6

def calcula_assinatura(texto):
    sentenca = separa_frases(texto)
    n_sentencas = 0
    soma_carac = 0
    frases =[]

    for i in range(len(sentenca)):
        aux = separa_frases(sentenca[i])
        frases.append(aux)
        n_sentencas += 1
        soma_carac = soma_carac + len(sentenca[i])
    
    palavras = []
    n_frases = 0
    soma_carac_frase = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            aux_palavra = separa_palavras(frases[linha][coluna])
            palavras.append(aux_palavra)
            n_frases += 1
            soma_carac_frase += len(frases[linha][coluna])
    
    matriz_lista = []
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            matriz_lista.append(palavras[linha][coluna])
    palavras = matriz_lista[:]

    letras = 0
    total_palavras = len(palavras)
    for l in range(len(palavras)):
        for c in range(len(palavras[l])):
            letras = letras + len(str(palavras[l][c]))
    
    wal = letras / total_palavras
    ttr = n_palavras_diferentes(palavras) / total_palavras
    hlr = n_palavras_unicas(palavras) / total_palavras
    sal = soma_carac / n_sentencas
    sac = n_frases / n_sentencas
    pal = soma_carac_frase / n_frases
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    assinaturas = []
    for i in textos:
        assinaturas.append(calcula_assinatura(i))

    similaridade = []
    for i in assinaturas:
        similaridade.append(compara_assinatura(ass_cp, i))

    maior = similaridade[0]
    posicao = 0
    for i in range(len(similaridade)):        
        if similaridade[i] > maior:
            maior = similaridade[i]
            posicao = i

    return posicao

def final():
    ass_cp = le_assinatura()
    textos = le_textos()
    
    return  print("O autor do texto " , avalia_textos(textos, ass_cp), " está infectado com COH-PIAH")
