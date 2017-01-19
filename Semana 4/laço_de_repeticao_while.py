'''
while condição:
    comando1
    comando2
comando 3
'''

# Potencias
i = 0
while i<= 10:
    print(2 ** i)
    i = i + 1

# Soma de numeros
margem = int(input('Quantos numeros você quer somar?: '))
soma = 0
cont = 0
while cont < margem:
    valor = int(input('Digite um valor a ser somado: '))
    soma = soma + valor
    cont += 1
print('A soma dos valores digitados foi igual a:', soma)