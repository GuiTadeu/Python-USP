def fatorial(x):
    cont = x - 1
    fatorial = x
    while cont >= 1:
        fatorial = fatorial * cont
        cont -= 1
    return fatorial

numero_n = int(input('Digite o valor do Numero N: '))
classe_k = int(input('Digite o valor da Classe K: '))
coeficiente_binomial = fatorial(numero_n) // (fatorial(classe_k) * fatorial(numero_n - classe_k))

print('Seu Coeficiente Binomial é:', coeficiente_binomial)

# Testes Automatizados
def testa_fatorial():
    if fatorial(1) == 1:
        print('Funciona para 1')
    else:
        print('Não funciona para 1')
    if fatorial(0) == 1:
        print('Funciona para zero')
    else:
        print('Não funciona para zero')