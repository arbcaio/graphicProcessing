import numpy as np
from primeiraEntrega.intersecoes import Esfera, Plano
from triangulo import Triangulo, Ponto, Vetor, Raio
from primeiraEntrega.camera import Camera


def trace(triangulos: list[Triangulo], raio: Raio):
    s = []

    for triangulo in triangulos:
        t = triangulo.intersect(raio)

        if t != float('inf'):
            print('achou')
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
    # intersecoes[0, 0] = E - distancia * w + escala * (((v_res - 1) / 2) * v - ((h_res - 1) / 2) * u) -> expressão
    a = (v_res - 1) / 2
    b = (h_res - 1) / 2
    c = v.produto_por_escalar(a) - u.produto_por_escalar(b)
    c = c.produto_por_escalar(escala)
    d = w.produto_por_escalar(distancia)
    vetor_soma = d + c
    intersecoes[0, 0] = E.sub_vetor(vetor_soma).coordenadas  # expressão simplificada

    # varrer pixels da imagem
    for i in range(v_res):
        for j in range(h_res):
            # move na direcao u e v multiplicando pelos indices e por s
            # intersecoes[i, j] = intersecoes[0, 0] + escala * (u.produto_por_escalar(j) - v.produto_por_escalar(i))
            uv = u.produto_por_escalar(j) - v.produto_por_escalar(i)
            uve = uv.produto_por_escalar(escala)
            intersecoes[i, j] = intersecoes[0, 0] + uve.coordenadas
            dir_raio = Vetor(*(intersecoes[i, j] - E.coordenadas))
            loc_raio = E
            raio = Raio(loc_raio, dir_raio)
            imagem[i, j] = cast(triangulos, raio, cor_fundo)

    # retorna imagem com cor normalizada
    return imagem / 255
