# Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
## Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

# Objetivo

# Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

# Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

# Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida;
## Caso contrário, o computador toma a inciativa de começar o jogo.
### Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

# Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

# Seu Programa

# Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.

# Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho funcione corretamente.

# O programa deve implementar:

# Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.
## Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
### Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
#### Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.

# Cuidado: o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função). Se seu programa usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.

# Campeonatos

# Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma

# Placar: Você ??? X ??? Computador

tipo_jogo = 0

def computador_escolhe_jogada(n, m):

    # Vez do computador:
    print("Vez do Computador!")

    # Pode retirar todas as peças?
    if n <= m:

        # Retira todas as peças e ganha o jogo:
        return n

    else:

        # Verfifica se é possível deixar uma quantia multipla de m+1:
        quantia = n % (m+1)

        if quantia > 0:
            return quantia

        # Não é, então tire m peças:
        return m

def usuario_escolhe_jogada(n, m):

    # Vez do usuário:
    print("Sua vez!\n")

    # Define o número de peças do usuário:
    jogada = 0

    # Enquanto o número não for válido:
    while jogada == 0:

        # Solicita ao usuário quantas peças irá tirar:
        jogada = int(input("Quantas peças irá tirar?"))

        # Condições: jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:

            # Valor inválido, continue solicitando ao usuário:
            jogada = 0

    # Número de peças válido, então retorne-o:
    return jogada

def partida():

    print(" ")

    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True

    # Decide quem iniciará o jogo:
    if n % (m+1) == 0:
        is_computer_turn = False
    
    # Execute enquanto houver peças no jogo:
    while n > 0:

        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))

        # Retira as peças do jogo:
        n = n - jogada

        # Mostra o estado atual do jogo:
        print("Restam apenas {} peças em jogo.\n".format(n))

    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def campeonado():

    # Pontuações:
    usuario = 0
    computador = 0

    # Executa 3 vezes:
    for _ in range(3):

        # Executa a partida:
        vencedor = partida()

        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1

    # Exibe o placar final:
    print("Placar final: Você {} x {} Computador".format(usuario, computador))

# Enquanto não for uma opção válida:
while tipo_jogo == 0:

    # Menu de opções:
    print("Bem vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")

    # Solicita a opção ao usuário:
    tipo_jogo = int(input("Sua opção: "))
    print(" ")

    # Decide o tipo de jogo:
    if tipo_jogo == 1:
        print("Você escolheu partida isolada.")
        partida()
        break
    if tipo_jogo == 2:
        print("Você escolheu um campeonato.")
        campeonado()
        break
    else:
        print("Opção inválida.")
        tipo_jogo = 0
    
