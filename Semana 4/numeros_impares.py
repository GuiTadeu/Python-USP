numero = int(input('Digite o valor de n: '))
cont = 0
impares = 1
while cont < numero:
    if not (impares % 2 == 0):
        print(impares)
    impares += 2
    cont = cont + 1