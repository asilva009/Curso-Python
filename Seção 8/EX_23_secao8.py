def triangulo_lateral(n):
    linha = ''
    for i in range(2 * n - 1):
        if i < n:
            linha = linha + (i+1) * '*' + '\n'
        else:
            linha = linha + (2 * n - (i+1)) * '*' + '\n'
    return linha


num = int(input('Digite um número: '))
print(triangulo_lateral(num))


