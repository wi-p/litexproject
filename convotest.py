# Exemplo de filtro convolucional aplicado a imagens


# filtro que descreve uma curva preta em um fundo branco
filter = [
    [0, 0, 0, 0, 0, 30, 0],
    [0, 0, 0, 0, 30, 0, 0],
    [0, 0, 0, 30, 0, 0, 0],
    [0, 0, 0, 30, 0, 0, 0],
    [0, 0, 0, 30, 0, 0, 0],
    [0, 0, 0, 30, 0, 0, 0],
    [0, 0, 0,  0, 0, 0, 0]
]

# representacao de uma imagem com curva
receptiveFilter = [
    [0, 0, 0, 0,  0,  0, 30],
    [0, 0, 0, 0, 50, 50, 50],
    [0, 0, 0, 20, 50, 0, 0],
    [0, 0, 0, 50, 50, 0, 0,],
    [0, 0, 0, 50, 50, 0, 0,],
    [0, 0, 0, 50, 50, 0, 0,],
    [0, 0, 0, 50, 50, 0, 0,],    
]

# inversao do da imagem para aplicar a convolucao
reverseReceptiveFilter = []

for i in range(7):
    reverseReceptiveFilter.append([])

    for j in range(7):
        reverseReceptiveFilter[i].append(receptiveFilter[i][-j - 1])

conv = [] # convolucao

for i in range(7):
    for j in range(7):
        pass