soma = 0
media = 0
print('Digite 10 números inteiros: ')
for numero in range(1, 11):
    num = int(input())
    soma = soma + num
media = soma / 10
print(f'Média = {media}')
