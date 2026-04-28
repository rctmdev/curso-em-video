frase = str(input('Digite uma frase: '))
framod = frase.strip().upper().replace(' ', '')
inverso = framod [::-1]
print('O inverso de {} é {}'.format(framod, inverso))
if framod == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

