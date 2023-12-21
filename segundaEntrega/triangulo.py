from primeiraEntrega.vetor import Vetor
from primeiraEntrega.pontos import Ponto
from raio import Raio
import uuid


class Triangulo:
    def __init__(self, pontos, cor):
        self.pontos = pontos
        self.cor = cor
        self.id = uuid.uuid4()

        aresta1 = pontos[1] - pontos[0]
        aresta2 = pontos[2] - pontos[1]

        self.vetor1 = Vetor(*aresta1.coordenadas)
        self.vetor2 = Vetor(*aresta2.coordenadas)
        self.normal = self.vetor1.produto_vetorial(self.vetor2)

    def intersect(self, raio: Raio):
        epsilon = 1e-6  # Valor pequeno para tratamento de erros de ponto flutuante

        # Verificando se o raio é paralelo ao triângulo
        h = raio.dir.produto_vetorial(self.vetor2)
        a = self.vetor1.produto_escalar(h)

        if abs(a) < epsilon:  # se a está próximo de zero
            return None  # raio é paralelo ao triângulo

        # calcular paramêtro u
        f = 1.0 / a
        s = raio.loc - self.pontos[0]
        u = f * (s.produto_escalar(h))

        # verificar se u está no intervalo [0,1]
        if u < 0.0 or u > 1.0:
            return float('inf')  # Ponto de interseção fora do triângulo

        # calcular parâmetro v
        q = s.produto_vetorial(self.vetor1)
        v = f * (raio.dir.produto_escalar(q))

        if v < 0.0 or u + v > 1.0:
            return float('inf')  # Ponto de interseção fora do triângulo

        # Parâmetro t para a interseção (distância)
        t = f * (self.vetor2.produto_escalar(q))

        if t > epsilon:
            '''ponto_intersecao = raio.loc + (raio.dir.coordenadas * t)
            ponto_intersecao = Ponto(*ponto_intersecao)
            return ponto_intersecao'''
            return t, self.id
        else:
            return float('inf')  # Interseção ocorre atrás da origem do raio

    def __repr__(self):
        return f'Triangulo {self.id}:\nPontos: {self.pontos}\nArestas: A = {self.vetor1}; B = {self.vetor2}'



