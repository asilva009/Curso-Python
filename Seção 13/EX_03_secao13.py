texto = input('Qual arquivo quer consultar o número de vogais?')
vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'ü']
qtd = 0

with open(texto) as arquivo:
    text = (arquivo.read()).lower()
    for i in text:
        if i in vogais:
            qtd += 1
print(f'Este texo possui {qtd} vogais')





