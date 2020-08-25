def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma


num = int(input('Digite um número inteiro positivo: '))
print(somatorio(num))

