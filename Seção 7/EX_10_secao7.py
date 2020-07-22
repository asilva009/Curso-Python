notas = []
soma = 0
media = 0
for i in range(15):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas.append(nota)
for valor in notas:
    soma = soma + valor
media = soma / 15
print(f'Média = {media:.2f}')
