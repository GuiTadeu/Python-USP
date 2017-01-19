def vogal(letra):
    if letra.lower() == 'a':
        return True
    elif letra.lower() == 'e':
        return True
    elif letra.lower() == 'i':
        return True
    elif letra.lower() == 'o':
        return True
    elif letra.lower() == 'u':
        return True
    else:
        return False

letra_vogal = vogal(input('Digite uma letra: '))
print(letra_vogal)
