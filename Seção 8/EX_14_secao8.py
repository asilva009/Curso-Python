def consumo_auto(distancia, qtd_litros):
    consumo = distancia / qtd_litros
    if consumo < 8:
        return f'Consumo = {consumo:.1f} Km/l -> Venda o carro!'
    elif consumo <= 12:
        return f'Consumo = {consumo:.1f} Km/l -> Econômico!'
    return f'Consumo = {consumo:.1f} Km/l -> Super Econômico!'
