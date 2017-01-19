# Dado um numero tem que dizer se ele tem dois digitos adjacentes iguais
numero = int(input('Digite um numero: '))

numero_inteiro = numero // 10
n1 = numero % 10
n2 = numero_inteiro % 10

adjacente = False
while not adjacente and numero_inteiro != 0:
    if n1 == n2:
        adjacente = True
    else:
        n1 = numero_inteiro % 10
        numero_inteiro = numero_inteiro // 10
        n2 = numero_inteiro % 10
        adjacente = False

if adjacente:
    print('Sim')
else:
    print('Não')





