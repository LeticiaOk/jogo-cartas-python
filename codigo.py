import random
from time import sleep
bot = []
jogador = []
baralho_individual = []
carta = 0
soma = 0

print("\033[35mAS CARTAS FORAM DISTRIBUÍDAS\033[m")
sleep(1)

while len(bot) < 2:
    carta = random.randint(1,11)

    if carta not in baralho_individual:
        bot.append(carta)
        baralho_individual.append(carta)

while len(jogador) < 2:
    carta = random.randint(1,11)

    if carta not in baralho_individual:
        jogador.append(carta)
        baralho_individual.append(carta)

print("\n\033[32mSeu Baralho:\033[m ?", end=" ")
for c, v in enumerate(jogador):   
    if c != 0:
        soma += v
        print(v, end=" ")
        
print(f"\n\033[32mSeu Total: \033[m?+{soma}/21")
sleep(2)
print("\n\033[31mBot Baralho:\033[m ?", end=" ")
for c, v in enumerate(bot):   
    if c != 0:
        soma += v
        print(v, end=" ")
        
print(f"\n\033[31mBot Total: \033[m?+{soma}/21")
sleep(2)


def jogador_vez():
    print("\n\033[35mSUA VEZ\033[m")
    jogador_resposta = input("\033[34mComprar \033[33m[C]\033[m \033[34mou Permanecer \033[33m[P]: \033[m")
    if jogador_resposta == "C":
        adicionado = False
        while adicionado == False:
            carta = random.randint(1,11)
            if carta not in baralho_individual:
                jogador.append(carta)
                adicionado = True
                print(f'\033[30mAdicionado a carta {carta} ao seu baralho.\033[m')
    else:
        print("\033[30mVoce permaneceu com o baralho atual.\033[m")

    print("\n\033[32mSeu Baralho:\033[m ?", end=" ")
    for c, v in enumerate(jogador):   
        if c != 0:
            soma += v
            print(v, end=" ")
        
    print(f"\n\033[32mSeu Total: \033[m?+{soma}/21")
    sleep(2)

def bot_vez():
    print("\033[35mVEZ DO BOT\033[m")
    bot_resposta = ""
    if sum(bot) < 19:
        bot_resposta = "C"
    if bot_resposta == "C":
        adicionado = False
        while adicionado == False:
            carta = random.randint(1,11)
            if carta not in baralho_individual:
                bot.append(carta)
                adicionado = True
                print(f'\033[30mAdicionado a carta {carta} ao baralho do bot.\033[m')
    else:
        print("\033[30mO bot permaneceu com o baralho atual\033[m")
    for c, v in enumerate(bot):
        if c != 0:
            print(v, end=" ")
    #print(bot)


jogador_resposta = ""
bot_resposta = ""

while "C" not in jogador_resposta and "C" not in bot_resposta:
    jogador_vez()
    bot_vez()
