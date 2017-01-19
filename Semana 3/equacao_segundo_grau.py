# Precisamos inmportar a bilbioteca Math
# Square Root in Python: math.sqrt(x)
import math

# Como o programa funcionara?
# Recebra 3 valores: A, B, C
# Usar a formula de Bhaskara para imprimir as raizes
# Se Delta for menor que 0, Não tem raizes reais
# Se Delta for 0, uma raiz real
# Se Delta for maior que 0, duas raizes reais

def baskara(a,b,c):
    delta = (b ** 2) - (4 * a * c)
    baskara = ((-b + math.sqrt(delta)) / (2 * a))
    return baskara

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c)

if delta<0:
    print('\nesta equação não possui raízes reais')

elif delta==0:
    x = baskara(a,b,c)
    print('\na raiz desta equação é', x)

elif delta>0:
    x = baskara(a,b,c)
    y = ((-b - math.sqrt(delta)) / (2 * a))
    if x <= y:
        print('\nas raízes da equação são', x, 'e', y)
    else:
        print('\nas raízes da equação são', y, 'e', x)
