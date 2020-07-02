numero = int(input('Digite um número: '))
if numero < 0:
    print('Número inválido')
else:
    raiz_quadrada = numero ** (1/2)
    print(f'Raiz quadrada = {raiz_quadrada}')
