# Semana 6
# Programa completo - jogo do NIM
# Ana Clara Barbeta


# N é o número inicial de peças
# M é o número máximo de peças a serem retiradas
# Se N é múltiplo de (M+1), player começa. Se não for, PC começa
#computador sempre deixa múltiplo de (m+1) no jogo


def partida():
    #solicitar valores
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    #definir quem vai começar e controles:
    comeca_player = False
    comeca_PC = False
    if n % (m+1) != 0:
        PC = True #controlar vez do computador
        comeca_PC = True 
        print("O computador começa!")
    else:
        PC = False
        comeca_player = True
        print("Você começa!")
    
    #definir jogadas
    while n > 0:
        if PC:
            jogada = computador_escolhe_jogada(n,m)
            PC = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n,m)
            PC = True
            print("Você retirou {} peças.".format(jogada))
    
        #peças restantes:
        n = n - jogada
        print("Restam apenas {} peças em jogo. \n".format(n))

    #Fim do jogo
    if PC:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def usuario_escolhe_jogada(n,m):
    #vez de player
    print("Sua vez! \n")

    jogada = 0

    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar?"))

        if jogada > n or jogada > m or jogada <1:
            print("Valor inválido. Tente novamente")
            jogada = 0
    return jogada

def computador_escolhe_jogada(n,m):
    print("Vez do computador! \n")

    if n < m:
        return n
    elif n % (m+1) > 0:
        return n % (m+1)
    else:
        return m

def campeonato():
    #pontuações iniciais
    pc = 0
    player = 0

    for i in range(1,4):
        print("**** Rodada {} **** \n".format(i))
        ganhou = partida()
        i +=1

        if ganhou == 1:
            player += 1
        else:
            pc += 1
    
    print ("**** Final do campeonato! ****")
    
    print("Placar final:  Você {} X {} Computador".format(player,pc))

# abertura do jogo
tipo = 0

while tipo == 0:
    #menu principal
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1- para jogar uma partida isolada")
    print("2- para jogar um campeonato")
    tipo = int(input(""))

    #definir modalidade
    if tipo == 1:
        print("Você escolheu uma partida isolada!")
        partida()
        break
    elif tipo == 2:
        print("Você escolheu um campeonato! \n")
        campeonato()
        break
    else:
        print("Opção inválida!")
        tipo == 0



