# Um numero só é primo se ele for divisivel apenas por 1 e por ele memsmo

numero = int(input('Digite um número inteiro: '))
cont = 2
aux = numero
primo = True

while primo and cont <= numero:

    if cont != 1 and cont != aux and aux % cont == 0:
        primo = False

    else:
        cont = cont + 1
        primo = True

if not primo:
    print('Não Primo')
else:
    print('Primo')




