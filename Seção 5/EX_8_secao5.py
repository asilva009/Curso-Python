print('Digite a 1ª e a 2ª nota: ')
nota1 = float(input())
nota2 = float(input())
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota1 + nota2) / 2
    print(f'Média = {media}')
else:
    print('Nota inválida')





