# Primeiro devemos testar se o numero é primo
# Caso ele não for devemos pegar o proximo numero primo depois dele
# Se ele for, retornamos ele mesmo

def primo(x):
    primo = True
    aux = x
    cont = 2
    while primo and cont <= aux:
        if cont != aux and aux % cont == 0:
            primo = False
        else:
          cont += 1
          primo = True
    return primo

def maior_primo(x):

    while not primo(x):
        x = x + 1
    return x


numero = int(input('Digite um Numero: '))

if primo(numero):
    print(numero)
else:
    print(maior_primo(numero))
