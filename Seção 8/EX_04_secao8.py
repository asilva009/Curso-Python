def quadrado_perfeito(numero):
    if int(numero) != numero or numero <= 0:
        return 'Número inválido! O número deve ser inteiro e maior que 0'
    raiz_quadrada = numero ** 0.5
    if raiz_quadrada == int(raiz_quadrada):
        return f'{numero} é quadrado perfeito de {int(numero**0.5)}'
    return f'{numero} não é um quadrado perfeito'
