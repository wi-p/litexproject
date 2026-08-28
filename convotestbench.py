# Arquivo de testagem

from migen import *
from migen.sim import run_simulation
from convoModule import ConvoModule


def testbench(dut):

    # Supondo imagem 6 * 5 = 30 pixels
    imagem = [
        [10, 24, 12, 16, 90],
        [81, 24, 17, 13, 25],
        [90, 89, 54, 21, 99],
        [87, 64, 41, 80, 99],
        [50, 10, 90, 32, 75],
        [60, 49, 35, 89, 20]
    ]

    print("\n\nIMAGEM\n\n ")
    for l in imagem:
        print(l)

    # Supondo filtro 3 * 3 = 9
    kernel = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print("\n\nKERNEL (FILTRO)\n\n")
    for l in kernel:
        print(l)

    print("\n\nKERNEL INVERTIDO\n\n")
    for l in range(len(kernel)):
        for c in range(len(kernel)):
            print(kernel[c][l], end=" ")
        print("")

    # Carregando imagem no dut (modulo)
    for l in range(6):
        for c in range(5):
            indice = l * 5 + c 

            # o comando yield e usado para ler e atribuir dados com base no clock
            yield dut.imagem[indice].eq(imagem[l][c])

    # Carregando kernel no dut (modulo)
    for l in range(3):
        for c in range(3):
            indice = l * 3 + c 

            # Atribuindo valor
            yield dut.kernel[indice].eq(kernel[l][c])

    yield # esperar um ciclo de clock

    resultado = [] # Imagem convolucionada

    for l in range(8):
        linha = []
        for c in range(7):
            indice = l * 7 + c 
            valorIndice = yield dut.saidaConvo[indice]

            linha.append(valorIndice)

        resultado.append(linha)

    print("\n\nMOSTRANDO IMAGEM CONVOLUCIONADA\n\n")

    for linha in resultado:
        print(linha)

dut = ConvoModule()

run_simulation(dut, testbench(dut), vcd_name = "convoucao.vcd")