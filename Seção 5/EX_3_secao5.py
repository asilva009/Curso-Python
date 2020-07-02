numero = float(input('Digite um número real: '))
if numero < 0:
    quadrado = numero ** 2
    print(f'Quadrado = {quadrado}')
else:
    raiz_quadrada = numero ** (1/2)
    print(f'Raiz Quadrada = {raiz_quadrada}')
