def tipo_de_triangulo(lado1, lado2, lado3):
    lados = lado1, lado2, lado3
    for lado in lados:
        if lado <= 0:
            return 'Todos os lados devem ter valor > 0'
    if lado1 >= lado2 + lado3:
        return 'As medidas dos lados não correspondem a um triângulo'
    elif lado2 >= lado1 + lado3:
        return 'As medidas dos lados não correspondem a um triângulo'
    elif lado3 >= lado1 + lado2:
        return 'As medidas dos lados não correspondem a um triângulo'
    elif lado1 == lado2 == lado3:
        return 'Triângulo Equilátero'
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        return 'Triângulo Escaleno'
    return 'Triângulo Isósceles'
