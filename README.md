# Projeto: Jogo da Velha em Python

## Descrição do Projeto

Este projeto foi desenvolvido como parte da APS (Atividade Prática Supervisionada) da disciplina de **Laboratório de Programação**. A solução consiste na implementação de um **Jogo da Velha** utilizando a linguagem Python. O jogo permite a participação de dois jogadores, que, alternadamente, escolhem as posições no tabuleiro para marcar suas jogadas. Caso um jogador tente selecionar uma posição já ocupada, o sistema não permitirá a jogada.

Cada partida será salva em um arquivo de texto contendo as seguintes informações:
- Nomes dos jogadores.
- Placar da partida.
- Estado final do tabuleiro.

O jogo segue as regras clássicas, onde o objetivo é formar uma linha com três marcas (X ou O) de maneira contínua, seja horizontalmente, verticalmente ou diagonalmente.

## Funcionalidades
- Dois jogadores alternam turnos para jogar.
- Verificação automática de vitórias e empates.
- Proibição de jogadas em posições já ocupadas.
- Exibição do tabuleiro atualizado a cada jogada.
- Salvamento do resultado final da partida, incluindo o tabuleiro e placar, em um arquivo `.txt`.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Ambiente de Desenvolvimento**: Visual Studio Code
- **Versão do Python**: 3.11.9

## Estrutura do Projeto

O projeto foi modularizado para manter o código organizado e de fácil manutenção:

- **`main.py`**: Controla o fluxo principal do jogo, interação com os jogadores e gerenciamento das rodadas.
- **`game_functions.py`**: Contém as funções principais que realizam a lógica do jogo, como inicialização do tabuleiro, verificação de vitória/empate, e exibição do tabuleiro.

## Exemplo de Saída

Ao final de cada partida, o resultado é salvo em um arquivo de texto com o seguinte formato:

