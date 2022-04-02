import random
from time import sleep

print("\033[1;30;45m------------------Jokenpô------------------\033[m")
print("Escolha o número respectivo:")

itens = ("PEDRA", "PAPEL", "TESOURA")
sorteio = random.randint(0,2)

print("\033[1;30m[0] - PEDRA\033[m")
print("\033[1;30m[1] - PAPEL\033[m")
print("\033[1;30m[2] - TESOURA\033[m")

while True:
    try:
        escolha_usuario = int(input("Qual a sua jogada?"))
        break
    except:
        print("\033[1;31mJogada inválida\033[m")
        continue

sleep(1)
print("\033[1;34mJO\033[m")
sleep(1)
print("\033[1;34mKEN\033[m")
sleep(1)
print("\033[1;34mPÔ\033[m")
sleep(1)

print("-----------------------------------------")
print("Máquina escolheu: \033[1;30m{}\033[m".format(itens[sorteio]))
print("Sua jogada: \033[1;30m {}\033[m".format(itens[escolha_usuario]))
print("-----------------------------------------")

if sorteio == 0:
    if escolha_usuario == 0:
        print("\033[1;33mEMPATE\033[m")
    elif escolha_usuario == 1:
        print("\033[1;33mVOCÊ VENCEU!\033[m")
    elif escolha_usuario == 2:
        print("\033[1;33mMÁQUINA VENCEU!\033[m")

if sorteio ==1:
    if escolha_usuario == 1:
        print("\033[1;33mEMPATE\033[m")
    elif escolha_usuario == 0:
        print("\033[1;33mMÁQUINA VENCEU!\033[m")
    elif escolha_usuario == 2:
        print("\033[1;33mVOCÊ VENCEU!\033[m")

if sorteio == 2:
    if escolha_usuario == 2:
        print("\033[1;33mEMPATE\033[m")
    elif escolha_usuario == 0:
        print("\033MÁQUINA VENCEU!\033[m")
    elif escolha_usuario == 1:
        print("\033[1;33mMÁQUINA VENCEU!\033[m")





















