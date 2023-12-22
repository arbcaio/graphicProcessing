import numpy as np
import matplotlib.pyplot as plt

from primeiraEntrega.camera import Camera
from primeiraEntrega.pontos import Ponto
from primeiraEntrega.vetor import Vetor
from renderizar import render
from segundaEntrega.malhaTriangular import MalhaTriangular
from segundaEntrega.triangulo import Triangulo
import os


def readline(tipo):
    return map(tipo, input().split())


if __name__ == "__main__":

    # camera
    v_res, h_res = readline(int)  # 1 resolução
    Cx, Cy, Cz = readline(float)  # 2 coord da camera
    Mx, My, Mz = readline(float)  # 3 coord mira
    ux, uy, uz = readline(float)  # 4 vetor up
    r, g, b = readline(int)  # 5 cor de fundo
    s, d = readline(float)  # 6 escala e distancia
    C = Ponto(Cx, Cy, Cz)
    M = Ponto(Mx, My, Mz)
    up = Vetor(ux, uy, uz)
    cor_fundo = np.array((r, g, b))

    # malha
    num_triangulos, num_vertices = readline(int)
    r, g, b = readline(int)
    cor_malha = np.array((r, g, b))
    vertices = []
    for i in range(num_vertices):
        x, y, z = readline(float)
        vertices.append(Ponto(x, y, z))
    triangulos = []
    for i in range(num_triangulos):
        v1, v2, v3 = readline(int)
        tri = Triangulo((vertices[v1], vertices[v2], vertices[v3]), cor_malha)
        triangulos.append(tri)

    malha = MalhaTriangular(num_triangulos, num_vertices, vertices, triangulos, cor_malha)

    imagem = render(malha.triangulos, v_res, h_res, s, d, C, M, up, cor_fundo)
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_saida = os.path.join(diretorio_atual, 'saida.png')

    plt.imsave(caminho_saida, imagem)
