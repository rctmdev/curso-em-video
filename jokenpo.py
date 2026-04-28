from random import randint
from time import sleep 
itens = ('\033[31mPedra', '\033[31mPapel', '\033[31mTesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*13)
print('Computador jogou {}'.format(itens[computador]))
print('\033[mJogador jogou {}'.format(itens[jogador]))
print('\033[m-='*13)
if computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('\033[31mCOMPUTADOR VENCE')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('\033[31mJOGADOR VENCE')
else:
    print('\033[31mEMPATE')

    