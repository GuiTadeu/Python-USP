decrescente = True
anterior = int(input('Digite o primeiro numero da sequencia: '))
valor = 1
while valor != 0 and decrescente:
    valor = int(input('Digite o proximo numero da sequencia: '))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print('A sequencia está em ordem decrescente')
else:
    print('A sequencia não está em ordem decrescente')

#########################################################################

meuCartao = int(input("Digite o numero do seu cartão de crédito: "))
cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input('Digite o numero do proximo cartão: '))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print('O Bruteforce deu certo!')
else:
    print('O Bruteforece deu errado!')