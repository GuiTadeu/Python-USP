numero = int(input('Digite um número inteiro: '))
aux = numero
cont = 0
soma = 0

while cont <= len(str(aux)):
    soma = (numero % 10) + soma
    numero = numero // 10
    cont = cont + 1

print(soma)
