def maximo(x,y):
    if x > y:
        return x
    else:
        return y

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
maior = maximo(n1,n2)
print(maior)