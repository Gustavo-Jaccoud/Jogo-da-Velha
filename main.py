from game_functions import *
# Inicializa as variaveis do programa 
pontos_jogador_1 = 0
pontos_jogador_2 = 0
nome_jogador_1 = input("Qual o nome do jogador 1? ")
nome_jogador_2 = input("Qual o nome do jogador 2? ")
    
while True:
        tabuleiro = CriarTabuleiro()
        vez_do_jogador = nome_jogador_1
        
        while True:
            print(ExibirPlacar(nome_jogador_1, nome_jogador_2, pontos_jogador_1, pontos_jogador_2))
            ExibirTabuleiro(tabuleiro)
            
            if vez_do_jogador == nome_jogador_1:
                jogador = 'X'
                print(f"\nVez de {nome_jogador_1}")
            else:
                jogador = 'O'
                print(f"\nVez de {nome_jogador_2}")
            
            while True:
                try:
                    linha = int(input(f"digite a linha de sua jogada (1, 2 ou 3): "))
                    coluna = int(input(f"Digite a coluna de sua jogada (1, 2 ou 3): "))
                    if ModificarTabuleiro(tabuleiro, jogador, linha, coluna):
                        break
                    print("Somente valores validos")
                except ValueError:
                    print("Entrada inválida! Digite números inteiros para linha e coluna.")
            
            if VerificarGanhador(tabuleiro, jogador):
                ExibirTabuleiro(tabuleiro)
                resultado = f"{vez_do_jogador} Ganhou!"
                if jogador == 'X':
                    pontos_jogador_1 += 1
                else:
                    pontos_jogador_2 += 1
                break
            
            if all(tabuleiro[linha][coluna] != ' ' for linha in range(3) for coluna in range(3)):
                ExibirTabuleiro(tabuleiro)
                resultado = "Empate!"
                break
            
            vez_do_jogador = AlternarTurno(vez_do_jogador,nome_jogador_1,nome_jogador_2)
        print(resultado)
        SalvarJogo(tabuleiro,resultado,ExibirPlacar(nome_jogador_1, nome_jogador_2, pontos_jogador_1, pontos_jogador_2))
        continuar = input("Deseja continuar? (S/N)")
        if continuar == "N" or continuar=="n":
            break
