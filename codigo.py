import random
from time import sleep
bot = []
player = []
indi_deck = []
hide = "on"
bet = 0
score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
score[7] = 'kill'
move = 7

while True:
    # APOSTA VAI AUMETANDO DE 2 EM 2 NO DECORRRER DAS RODADAS
    bet+=2

    # INÍCIO DE PARTIDA
    print("\n\033[35mAS CARTAS FORAM DISTRIBUÍDAS\033[m")
    sleep(1.5)
    
    # FUNÇÃO DO PLACAR
    def score_def():
        # Mostra o desenho do placar na tela 
        print("\n\033[31m", end="")
        for c, v in enumerate(score):
            if c == 0 and move != 0:
                print("JOGADOR ", end= " ")
            elif c == 14 and move != 14:
                print(" BOT")
            elif c == move:
                # A caveira irá se mover e ficar posicionada de acordo com o resultado final de cada rodada.
                # Quem controla isso é o valor da variavel 'move'.
                print("☠︎", end=" ")
            else:
                print(".", end= " ")
        print("\033[m")

    # CHAMANDO A FUNÇÃO DO PLACAR
    score_def()

    # MOSTRANDO A APOSTA DA RODADA
    print(f"\033[33mAPOSTA: \033[m{bet}")


    sleep(1.5)
    # FUNÇÃO DISTRIBUINDO CARTAS
    def deal_cards(turn):
        #  Cada jogador recebe inicialmente duas cartas aleatórias
        while len(turn) < 2:
            #  Gera cartas aleatorias usando numero randômico
            card = random.randint(1,11)

            # Adicionando cartas no baralho caso não estejam nos baralhos individuais de cada jogador
            if card not in indi_deck:
                turn.append(card)
                indi_deck.append(card)

    # CHAMANDO FUNÇÃO DISTRIBUINDO CARTAS
    deal_cards(player)
    deal_cards(bot)


    # FUNÇÃO MOSTRANDO BARALHOS
    def show_deck(turn, name):
        deck_sum = 0
        global hide
        #  Se o valor de hide for "on" a primeira carta do bot ficará oculta
        if name == "BOT" and hide == "on":
            print(f"\n\033[36mBaralho {name}:\033[m ?", end=" ")
            # Mostrando informações do baralho
            for c, v in enumerate(turn):
                if c != 0: 
                    deck_sum += v
                    print(v, end=" ")
            print(f"\n\033[36mTotal {name}: \033[m?+{deck_sum}/21")

        # Se a soma do baralho do jogador for MAIOR que 21 a cor mudará para VERMELHO
        elif name == "JOGADOR" and sum(turn) > 21:
            # Mostrando informações do baralho
            print(f"\n\033[36mBaralho {name}:\033[m", end=" ")
            for c, v in enumerate(turn):   
                deck_sum += v
                print(v, end=" ")
            print(f"\n\033[36mTotal {name}: \033[m\033[31m{deck_sum}/21\033[m")
        
        # Se a soma do baralho do jogador for IGUAL que 21 a cor mudará para VERDE
        elif name == "JOGADOR" and sum(turn) == 21:
            # Mostrando informações do baralho
            print(f"\n\033[36mBaralho {name}:\033[m", end=" ")
            for c, v in enumerate(turn):   
                deck_sum += v
                print(v, end=" ")
            print(f"\n\033[36mTotal {name}: \033[m\033[32m{deck_sum}/21\033[m")

        else:
            # Mostrando informações do baralho
            print(f"\n\033[36mBaralho {name}:\033[m", end=" ")
            for c, v in enumerate(turn):   
                deck_sum += v
                print(v, end=" ")
            print(f"\n\033[36mTotal {name}: \033[m{deck_sum}/21")


    # FUNÇÃO RESULTADO DE ESCOLHA
    def choice_result(turn, choice, name):
        if choice == "C" and sum(turn) < 21:
            adicionado = False
            # Enquanto a variável for igual a "False" continuára gerando cartas aleatórias até que alguma seja adicionada e a variavel se torne verdadeira
            while adicionado == False:
                # Gerando carta aleatória para ser adicoonada
                card = random.randint(1,11)
                # Adicionando carta ao baralho caso ainda não esteja no baralho individual de cada jogador
                if card not in indi_deck:
                    turn.append(card)
                    indi_deck.append(card)
                    # Variavel se torna verdadeira assim que alguma carta é adicionada
                    adicionado = True
                    print(f'\033[30mAdicionado a carta {card} ao baralho do {name}.\033[m')
                    resp = "C"

        #  Caso o jogador tente comprar mais cartas já estando com a soma do baralho acima ou igual a 21 uma mensagem aparece e ele permanece com o baralho atual.
        elif choice == "C" and sum(turn) >= 21:
            print("\n\033[31mQuantidade máxima de pontos atingida!\n\033[m")
            print(f"\033[30mO {name} permaneceu com o baralho atual.\033[m")
            resp = "P"
        else: 
            print(f"\033[30mO {name} permaneceu com o baralho atual.\033[m")
            resp = "P"
        sleep(1.5)

        # Retorna a resposta C ou P
        return resp

    # fUNÇÃO VEZ DO JOGADOR
    def player_turn():  
        # CHAMANDO FUNÇÃO MOSTRANDO BARALHOS
        show_deck(player, "JOGADOR")
        show_deck(bot, "BOT")

        sleep(1.5)

        # MECANICA DO JOGADOR
        print("\n\033[35mSUA VEZ\033[m")
        # O jogador escolhe se deseja comprar ou permanecer o o baralho atual
        choice = input("\033[34mComprar \033[33m[C]\033[m \033[34mou Permanecer \033[33m[P]: \033[m")
        
        # Passando parâmetros paraa função de resultado de escolha
        resp = choice_result(player, choice, "jogador")
        
        # Retorna a resposta C ou P
        return resp

    
    # VEZ DO BOT
    def bot_turn():
        # MECANICA DO BOT
        print("\n\033[35mVEZ DO BOT\033[m")

        #  Caso a soma do baralho do bot seja maior ou igual a 19 ele irá permanecer com o baralho atual
        if sum(bot) < 19:
            choice = "C"
        else:
            choice = "P"

        # Passando parâmetros paraa função de resultado de escolha
        resp = choice_result(bot, choice, "bot")

        # Retorna a resposta C ou P
        return resp

    # Cada variável irá receber uma resposta C ou P 
    player_resp = player_turn()
    bot_resp = bot_turn()
    
    # Enquanto as respostas forem iguais a C (Comprar) a rodada continua até que ambas sejam iguais a P (Permaneer) e as cartas sejam reveladas
    while True:
        if player_resp == "P" and bot_resp == "P":
            break
        player_resp = player_turn()
        bot_resp = bot_turn()

    # Saindo do laço o valor da variável muda e a primeira carta do bot é revelada
    hide = "of"

    # REVELANDO AS CARTAS
    print("\n\033[35mAS CARTAS FORAM REVELADAS\033[m")

    # CHAMANDO A FUNÇÃO MOSTRAR BARALHO
    show_deck(player, "jogador")
    show_deck(bot, "bot")

    # Revelando o vencedor da rodada
    if (sum(player) == 21 and sum(player) < sum(bot)) or (sum(player) < 21 and sum(player) > sum(bot)) or (sum(player) < 21 and sum(bot) > 21) or (sum(player) > 21 and sum(bot) > 21 and sum(player) < sum(bot)) or (sum(player) == 21 and sum(bot) < 21): 
        print("\n\033[32mVocê venceu esta rodada.\033[m")
        result = "player"
        
    elif sum(player) == sum(bot):
        print("\n\033[33mO jogo empatou.\033[m")
        result = "tie"
    else:
        print("\n\033[31mO bot venceu esta rodada.\033[m")
        result = "bot"
    
    # MECÂNICA DO PLACAR
    if result == "player":
        # O move vai servir para dizer onde a caveira irá ficar posicionada, assim é SOMADO o index atual da palavra 'kill' (que simboliza a caveira) ao número da aposta atual.
        # Fazendo com que a caveira ande para direita (lado do bot)
        move =  score.index('kill') + bet
        # Condição para caso o resultado seja maior que 14 que é o último número da lista.
        if move > 14:
            move = 14
        
        # A variável índice recebe o index atual de 'kill' na lista.
        indice = score.index('kill')
        # O índice do score onde está a palavra 'kill' é subistiuído pelo número do index de 'kill'.
        score[indice] = score.index('kill')
        # E o índice, que é resultado da conta, será subistituído por 'kill'.
        score[move] = 'kill'

    # A mesma coisa é aplicada caso o bot vença a partida, com a diferença de que será SUBTRAÍDO do index atual da palavra 'kill' (que simboliza a caveira) o número atual da aposta. 
    # Fazendo com que a caveira ande para esquerda (lado do player)
    elif result == "bot":
        move =  score.index('kill') - bet
        if move < 0:
            move = 0
        indice = score.index('kill')
        score[indice] = score.index('kill')
        score[move] = 'kill'
    # Caso nenhum dos dois vença (empate) move continua sendo o mesmo index de 'kill'
    else:
        move = score.index('kill')
    
    # Resetando 
    player.clear()
    bot.clear()
    indi_deck.clear()
    hide = "on"
    aposta = 2

    sleep(1.5)

    #  Resultado final da partida. Caso a caveira chegue a uma das extremidades da lista, ou seja no JOGADOR ou no BOT, a partida acaba revelando o vencedor.
    if move == 14:
        score_def()
        print('\n\033[32mPARABÉNS VOCÊ VENCEU!\033[m')
        break
    
    elif move == 0:
        score_def()
        print("\n\033[31mVOCÊ PERDEU!\033[m")
        break


print("\n\033[30mFIM DE JOGO\033[m")
