numero = int(input('Digite um número inteiro: '))

# O Operador // deixa o 8/5 igual a 1, ele tira o 1,6, deixa a parte inteira
# O operador % devolve o resto da divisão, 1 ou 0

# Cortando o numero nos dois ultimos digitos
corte = numero % 100
# Transformando 15 em 1.5 e pegando a parte inteira
dezena = corte // 10

print('O dígito das dezenas é', dezena)
