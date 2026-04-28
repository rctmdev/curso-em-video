n = int(input("Digite o valor de N: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"\nOs {n} primeiros elementos da Sequência de Fibonacci:")

    a, b = 0, 1
    contador = 0

    while contador < n:
        print(a, end=" ")
        a, b = b, a + b
        contador += 1

    print()


