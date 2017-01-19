import math

Xa = int(input('Digite um numero (Xa): '))
Ya = int(input('Digite um numero (Ya): '))
Xb = int(input('Digite um numero (Xb): '))
Yb = int(input('Digite um numero (Yb): '))

distancia = math.sqrt(((Xb - Xa)**2) + ((Yb - Ya) **2))

if distancia >= 10:
    print('Longe')
else:
    print('Perto')

