# source: https://www.allaboutcircuits.com/technical-articles/two-dimensional-convolution-in-image-processing/


# representacao da imagem
image = [
    [25, 100, 75, 49, 130],
    [50,  80,  0, 70, 100],
    [ 5,  10, 20, 30, 100],
    [60,  50, 12, 24,  32],
    [37,  53, 55, 21,  90]
]

# Kernel (filtro usado para fazer a convolucao)
kernel = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
]

provKernel = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# inversao da matriz kernel
print("A matriz kernel inveritda é: ")
for i in range(len(kernel)):
    for j in range(len(kernel[i])):
        provKernel[i][j] = kernel[j][i]
        print(provKernel[i][j], end=" ")

    print()

# deslizamento da matriz kernel sobre a imagem
