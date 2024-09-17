# Função  que retorna a string do placar
def ExibirPlacar(nome_jogador_1,nome_jogador_2,pontos_jogador_1,pontos_jogador_2):

    return f"{nome_jogador_1}({pontos_jogador_1}) X {nome_jogador_2}({pontos_jogador_2})"

# Função que incializa um tabuleiro vazio 
def CriarTabuleiro():

    tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]
    return tabuleiro

# Função que exibe na tela o tabuleiro 
def ExibirTabuleiro(tabuleiro):
    
    for linha in tabuleiro:
        print(" | ".join(linha))

# Função que verica se a casa esta disponivel no tabuleiro
def VerificarTabuleiro(tabuleiro,linha,coluna):

    if 1 <= linha < 4 and 1 <= coluna < 4 and tabuleiro[linha-1][coluna-1] == ' ':
        return True
    else:
        return False

# Função que modifica o tabulerio com a jogada do jogador 
def ModificarTabuleiro(tabuleiro,jogador,linha,coluna):

    if VerificarTabuleiro(tabuleiro,linha,coluna):
        tabuleiro[linha-1][coluna-1]=jogador
        return True
    
    return False

# Função que verifica as condições de ganhar 
def VerificarGanhador(tabuleiro,jogador):

    for linha in tabuleiro:
        if linha.count(jogador) == 3: 
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

# Função que alterna o turno dos jogadores 
def AlternarTurno(vez_do_jogador,nome_jogador_1,nome_jogador_2):
    if vez_do_jogador == nome_jogador_1:

        return nome_jogador_2 
    else: 
        return nome_jogador_1


# Função que armazena o jogo em um arquivo .txt
def SalvarJogo(tabuleiro,resultado,placar):
    with open('jogo_da_velha.txt', 'a') as file:
        file.write(str(placar)+"\n")
        for linha in tabuleiro:    
            file.write(" | ".join(linha)+"\n")
        file.write(str(resultado)+"\n-------------------\n")
        