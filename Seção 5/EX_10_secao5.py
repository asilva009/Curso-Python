sexo = input("Sexo: Masculino ou Feminino \n")
altura = float(input("Altura: "))
if sexo == "Masculino":
    peso = (72.7 * altura) - 58
    print(f"Peso ideal: {peso:.2f}kg")
else:
    peso = (62.1 * altura) - 44.7
    print(f"Peso ideal: {peso:.2f}kg")
