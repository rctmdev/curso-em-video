pe = float(input('Qual é seu peso? (km) '))
al = float(input('Qual é sua altura? (m) '))
imc = pe / (al ** 2) 
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5: 
    print('Voçê está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25: 
    print('PARABÉNS, você esta na faixa de PESO NORMAL')    
elif imc >= 25 and imc < 30:
    print('Voçê esta em SOBREPESO')
elif imc >= 30 and imc <= 40: 
    print('Voçê está em OBESIDADE!')   
else:
    print('Voçê está em OBESIDADE MÓRBIDA, cuidado!') 
    
            
