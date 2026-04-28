from time import sleep
from random import randint
jogo = []
print('-'*30)
print(f'{'JOGO NA MEGA SENA':^30}')
print('-'*30)
jogos = int(input('Quantos jogos voçê quer que eu sorteie? '))
print('-='*4,f' SORTEANDO {jogos} JOGOS ','-='*4)
for c in range(1,jogos+1):
    print(f'Jogo {c}: ', end='')
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    print(jogo)
    sleep(1)
    jogo.clear()
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
