with open("arquivo.txt", "w") as arquivo:
    while True:
        caracter = input("Entre com um caracter: ")
        if caracter != "O":
            arquivo.write(caracter)
            arquivo.write("\n")
        else:
            break

with open("arquivo.txt", "r") as arquivo:
    print(arquivo.read())
