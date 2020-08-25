def quantos_primos(numero):
    qtd = 0
    for i in range(2, numero):
        contador = 0
        for j in range(1, i + 1):
            if i % j == 0:
                contador = contador + 1
        if contador == 2:
            qtd = qtd + 1
    return f'Quantidade de primos abaixo de {numero} = {qtd}'


num = int(input('Informe um número: '))
print(quantos_primos(num))


