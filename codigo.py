import random
from time import sleep
bot = []
player = []
indi_deck = []
hide = "on"

# INÍCIO DE PARTIDA
print("\033[35mAS CARTAS FORAM DISTRIBUÍDAS\033[m")


# FUNÇÃO DISTRIBUINDO CARTAS
def deal_cards(turn):
    while len(turn) < 2:
        card = random.randint(1,11)

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
    if name == "BOT" and hide == "on":
        print(f"\n\033[36mBaralho {name}:\033[m ?", end=" ")
        for c, v in enumerate(turn):
            if c != 0: 
                deck_sum += v
                print(v, end=" ")
        print(f"\n\033[36mTotal {name}: \033[m?+{deck_sum}/21")

    elif name == "JOGADOR" and sum(turn) > 21:
        print(f"\n\033[36mBaralho {name}:\033[m", end=" ")
        for c, v in enumerate(turn):   
            deck_sum += v
            print(v, end=" ")
        print(f"\n\033[36mTotal {name}: \033[m\033[31m{deck_sum}/21\033[m")
    
    elif name == "JOGADOR" and sum(turn) == 21:
        print(f"\n\033[36mBaralho {name}:\033[m", end=" ")
        for c, v in enumerate(turn):   
            deck_sum += v
            print(v, end=" ")
        print(f"\n\033[36mTotal {name}: \033[m\033[32m{deck_sum}/21\033[m")


    else:
        print(f"\n\033[36mBaralho {name}:\033[m", end=" ")
        for c, v in enumerate(turn):   
            deck_sum += v
            print(v, end=" ")
        print(f"\n\033[36mTotal {name}: \033[m{deck_sum}/21")


# FUNÇÃO MECANICA ESCOLHA
def choice_result(turn, choice, name):
    if choice == "C" and sum(turn) < 21:
        adicionado = False
        while adicionado == False:
            card = random.randint(1,11)
            if card not in indi_deck:
                turn.append(card)
                indi_deck.append(card)
                adicionado = True
                print(f'\033[30mAdicionado a carta {card} ao baralho do {name}.\033[m')
                resp = "C"
    
    elif choice == "C" and sum(turn) >= 21:
        print("\n\033[31mQuantidade máxima de pontos atingida!\n\033[m")
        print(f"\033[30mO {name} permaneceu com o baralho atual.\033[m")
        resp = "P"
    else: 
        print(f"\033[30mO {name} permaneceu com o baralho atual.\033[m")
        resp = "P"
    sleep(1.5)
    return resp

    
   

# VEZ DO JOGADOR
def jogador_vez():  
    # CHAMANDO FUNÇÃO MOSTRANDO BARALHOS
    show_deck(player, "JOGADOR")
    show_deck(bot, "BOT")

    sleep(1.5)

    # MECANICA DO JOGADOR
    print("\n\033[35mSUA VEZ\033[m")
    choice = input("\033[34mComprar \033[33m[C]\033[m \033[34mou Permanecer \033[33m[P]: \033[m")
    resp =choice_result(player, choice, "jogador")
    
    return resp

 
# VEZ DO BOT
def bot_vez():
    # MECANICA DO BOT
    print("\n\033[35mVEZ DO BOT\033[m")
   
    if sum(bot) < 19:
        choice = "C"
    else:
        choice = "P"

    # CHAMANDO FUNÇÃO MECÂNICA DE ESCOLHA
    resp = choice_result(bot, choice, "bot")

    return resp

j = jogador_vez()
b = bot_vez()
    
while True:
    if j == "P" and b == "P":
        break
    j = jogador_vez()
    b = bot_vez()

hide = "of"

# REVELANDO AS CARTAS
print("\n\033[35mAS CARTAS FORAM REVELADAS\033[m")
show_deck(player, "jogador")
show_deck(bot, "bot")

# MECANICA DO RESULTADO
if (sum(player) == 21 and sum(player) < sum(bot)) or (sum(player) < 21 and sum(player) > sum(bot)) or (sum(player) < 21 and sum(bot) > 21):
    print("\n\033[32mPARABÉNS VOCÊ VENCEU!\033[m")
elif sum(player) == sum(bot):
    print("\n\033[33mO JOGO EMPATOU\033[m")
else:
    print("\n\033[31mVOCÊ PERDEU!\033[m")