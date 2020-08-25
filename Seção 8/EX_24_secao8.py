def triangulo(n):
    linha = ''
    p = '*'
    for i in range(2 * n - 1):
        linha = linha + (n - (i + 1)) * ' ' + p + '\n'
        if len(p) == 2 * n - 1:
            break
        else:
            p = p + 2 * '*'
    return linha



num = int(input('Digite um número: '))
print(triangulo(num))



