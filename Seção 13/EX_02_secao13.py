texto = input('Qual arquivo quer consultar o número de linhas? ')

with open(texto) as arquivo:
    print(f'O arquivo possui {len(arquivo.readlines())} linhas')
