def soma_entre(num1, num2):
    numeros = num1, num2
    for numero in numeros:
        if numero < 0 or numero != int(numero):
            return 'Os números devem ser inteiros positivos'
    soma = 0
    for valor in range(num1 + 1, num2):
        soma = soma + valor
    return f'A soma do números entre {num1} e {num2} é {soma}'
