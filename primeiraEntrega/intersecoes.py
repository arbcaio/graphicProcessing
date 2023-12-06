import numpy as np

class Esfera:
    def __init__(self, centro, raio, cor_rgb):
        self.centro = np.array(centro)
        self.raio = raio
        self.cor_rgb = np.array(cor_rgb)

class Plano:
    def __init__(self, ponto, vetor_normal, cor_rgb):
        self.ponto = np.array(ponto)
        self.vetor_normal = np.array(vetor_normal)
        self.cor_rgb = np.array(cor_rgb)

def intersecao_raio_esfera(origem_raio, direcao_raio, esfera):
    origem_raio = np.array(origem_raio)
    direcao_raio = np.array(direcao_raio)
    
    a = np.dot(direcao_raio, direcao_raio)
    oc = origem_raio - esfera.centro
    b = 2.0 * np.dot(oc, direcao_raio)
    c = np.dot(oc, oc) - esfera.raio ** 2
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return None  # Sem interseção
    else:
        t = (-b - np.sqrt(discriminante)) / (2*a)
        ponto_intersecao = origem_raio + t * direcao_raio
        return ponto_intersecao

def intersecao_raio_plano(origem_raio, direcao_raio, plano):
    origem_raio = np.array(origem_raio)
    direcao_raio = np.array(direcao_raio)
    numerador = np.dot(plano.vetor_normal, plano.ponto - origem_raio)
    denominador = np.dot(plano.vetor_normal, direcao_raio)

    if denominador == 0:
        return None  # Raio paralelo ao plano

    t = numerador / denominador
    if t < 0:
        return None  # Interseção atrás do raio

    ponto_intersecao = origem_raio + t * direcao_raio
    return ponto_intersecao

