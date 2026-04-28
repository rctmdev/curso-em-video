print('{:=^40}'.format(' LOJAS CAZZOLLI '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão 
[ 3 ] 2x cartão 
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1: 
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço - (preço / 10)))
elif opção == 2: 
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço - (preço * 0.05)))    
elif opção == 3: 
    print('Sua compra de R${:.2f} vai custar 2x parcelas de R${:.2f}.'.format(preço, preço / 2))
elif opção == 4: 
    qp = int(input('Quantas parcelas? '))  
    ju = preço * 0.2
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qp, (preço + ju)/qp))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no fial.'.format(preço, preço + ju))
else: 
    print('Opção INVÁLIDA!')    
      