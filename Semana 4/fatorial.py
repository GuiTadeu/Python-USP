# Fatorial de 5: 5x4x3x2x1

numero = int(input('Digite o valor de n: '))
cont = numero - 1
fatorial = numero

while cont >= 1:
    fatorial = fatorial * cont
    cont = cont - 1

print(fatorial)