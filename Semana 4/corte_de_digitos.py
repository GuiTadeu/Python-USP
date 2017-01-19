numero_digitado = int(input('Digite um numero para somar seus digitos: '))
numero_cortado = numero_digitado
i = 0
soma = 0
while i < len(str(numero_digitado)):
    soma = (numero_cortado % 10) + soma
    print(soma)
    numero_cortado = numero_cortado // 10
    print(numero_cortado)
    i += 1
print('A soma dos numeros foi igual a:',soma)
