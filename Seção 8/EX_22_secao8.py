def linha_com_exclamacao(n):
    linhas = ''
    lista = [i * '!' for i in range(1, n+1)]
    for i in lista:
        linhas = linhas + i + '\n'
    return linhas

print(linha_com_exclamacao(5))
