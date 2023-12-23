from primeiraEntrega.vetor import Vetor
from math import sqrt
from primeiraEntrega.pontos import Ponto
from raio import Raio
import uuid


class Triangulo:
    def __init__(self, pontos, cor):
        self.pontos = pontos
        self.cor = cor

        aresta1 = pontos[1] - pontos[0]
        aresta2 = pontos[2] - pontos[1]

        self.vetor1 = Vetor(*aresta1.coordenadas)
        self.vetor2 = Vetor(*aresta2.coordenadas)
        self.normal = self.vetor1.produto_vetorial(self.vetor2)

    def intersect(self, raio: Raio):
        epsilon = 1e-6

        h = raio.dir.produto_vetorial(self.vetor2)
        a = self.vetor1.produto_escalar(h)

        if -epsilon < a < epsilon:
            return False  # This ray is parallel to this triangle.

        f = 1.0 / a
        s = Vetor(*(raio.loc - self.pontos[0]).coordenadas)
        u = f * s.produto_escalar(h)

        if u < 0.0 or u > 1.0:
            return None

        q = s.produto_vetorial(self.vetor1)
        v = f * raio.dir.produto_escalar(q)

        if v < 0.0 or u + v > 1.0:
            return False

        # At this stage, we can compute t to find out where the intersection point is on the line.
        t = f * (self.vetor2.produto_escalar(q))

        if t > epsilon:  # ray intersection
            return True
        else:  # This means that there is a line intersection but not a ray intersection.
            return False

