def soma_algarismos(numero):
    soma = 0
    if numero > 0:
        num = list(str(numero))
        for number in range(len(num)):
            soma = soma + int(num[number])
        return f'A soma dos números é {soma}'
    else:
        return 'Número invalido'
