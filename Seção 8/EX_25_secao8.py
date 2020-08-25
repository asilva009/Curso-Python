def serie(n):
    s = [(valor ** 2 + 1) / (valor + 3) for valor in range(1, n + 1)]
    return round(sum(s), 2)


num = int(input('Digite um número: '))
print(serie(num))
