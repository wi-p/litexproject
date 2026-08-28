# Arquivo de definicao do modulo
from migen import *

class ConvoModule(Module): # classe para convolucao 2D (enre matrizes)
  # Dimensoes da imagem
  largImagem = 6
  compImagem = 5

  # Dimensoes do filtro
  largKernel = 3
  compKernel = 3

  # Dimensoes da imagem de saida (convolucionada)
  largConv = largImagem + largKernel - 1 # 8 pois o filtro add 2
  compConv = compImagem + compKernel - 1 # 7 pois o filtro add 2

  def __init__(self):
    # Sinais de entrada
    self.imagem = Array(
      # Sinal da imagem, nesse caso 30 bits/pixels
      Signal(8, name="EntradaImagem") for i in range(self.largImagem * self.compImagem)  # atributo name nao pode ter espacos
    )

    self.kernel = Array(
      # Sinal do Kernel, 9 bits na matriz filtro
      Signal(8, name = "EntradaKernel") for i in range(self.compKernel * self.largKernel)
    )
    # https://www.allaboutcircuits.com/uploads/articles/Fig2_2D_Conv.jpg

    # Sinais de saida (convolucao)
    # A imagem convolucionada tera 56 pixels, larg * comp
    self.saidaConvo = Array(Signal(20, name = "Saida") for i in range(self.compConv * self.largConv))

  # Logica combinacional

  ###
    # Deslizamento: https://www.allaboutcircuits.com/uploads/articles/Fig3ab_2D_Conv.jpg
    combinacao = []

    # Convolucao:  https://www.songho.ca/dsp/convolution/files/conv2dsep_eq01.png
    for i in range(self.largConv):
      for j in range(self.compConv):
        soma = 0 #Acumulador

        for k in range(self.largKernel):
          for l in range(self.compKernel):
            # Posicoes
            x = i - k 
            y = j - l 

            # Eliminando a ocorrencia de zeros ao redor
            if (
              x >= 0 and x < self.largImagem and y >= 0 and y < self.compImagem
            ):
              indiceImagem = x * self.compImagem  + y 

              # Fazendo o kernel (filtro deslizar sobre a imagem)
              indiceKernel = 1 * self.compKernel + k 

              soma += self.imagem[indiceImagem] * self.kernel[indiceKernel]

        indiceSaida = i * self.compConv + j 

        combinacao.append(self.saidaConvo[indiceSaida].eq(soma))

    self.comb += combinacao  