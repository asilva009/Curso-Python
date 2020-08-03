def notas_aluno(nota1, nota2, nota3, media='A'):
    if media == 'P':
        media_p = (nota1*5 + nota2*3 + nota3*2) / 10.0
        return f'Média Ponderada = {media_p}'
    media_a = (nota1 + nota2 + nota3) / 3.0
    return f'Média Aritmética = {media_a:.1f}'
