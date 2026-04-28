a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terçeiro segmento: '))
if a+b>c and a+c>b and b+c>a: 
   print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
   if a==b==c:
       print('EQUILÁTERO!') 
   elif a==b or a==c or b==c: 
       print('ISÓSCELES!')    
   else:
       print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')    
    
    