soma = 0
media = 0
qtde = 0
print('Digite 10 números inteiros: ')
for numero in range(1, 11):
    num = int(input())
    if num >= 0:
        soma = soma + num
        qtde = qtde + 1
media = soma / qtde
print(f'Média dos positivos = {media}')

