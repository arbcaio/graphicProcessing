import numpy as np
from primeiraEntrega.intersecoes import Esfera, Plano
from triangulo import Triangulo, Ponto, Vetor, Raio
from primeiraEntrega.camera import Camera


def trace(triangulos, raio: Raio):
    s = []

    for triangulo in triangulos:
        t, id = triangulo.intersect(raio)

        if t != float('inf'):
            s.append((t, triangulo))

    return s


def cast(triangulos, raio: Raio, cor_fundo):
    s = trace(triangulos, raio)
    s.sort()

    c = cor_fundo
    if len(s) != 0:
        primeiro = s[0][1]
        c = primeiro.cor

    return c  # cor de fundo ou o primeiro


def render(triangulos, v_res, h_res, escala, distancia, E: Ponto, L: Ponto, up: Vetor, cor_fundo):
    # normalizar w -> E - L
    w = E - L
    w = Vetor(*w.coordenadas)
    w = w.normalizar()

    # normalizar u -> produto vetorial (up, w)
    u = up.produto_vetorial(w)
    u = u.normalizar()

    v = w.produto_vetorial(u)

    intersecoes = np.zeros((v_res, h_res, 3))  # array de interseções inicializado com 0
    imagem = np.full((v_res, h_res, 3), cor_fundo)  # array da imagem inicializado com a cor de fundo

    # cálculo ponto de origem (inferior esquerdo)
    intersecoes[0, 0] = E - distancia * w + escala * (((v_res - 1) / 2) * v - ((h_res - 1) / 2) * u)

    # varrer pixels da imagem
    for i in range(v_res):
        for j in range(h_res):
            # move na direcao u e v multiplicando pelos indices e por s
            intersecoes[i, j] = intersecoes[0, 0] + escala * (j * u - i * v)
            dist_raio = Vetor(*(intersecoes[i, j] - E))
            loc_raio = E
            raio = Raio(loc_raio, dist_raio)
            imagem[i, j] = cast(triangulos, raio, cor_fundo)

    return imagem / 255
