import numpy as np, uuid
from primeiraEntrega.pontos import Ponto
from triangulo import Triangulo
from raio import Raio


class MalhaTriangular:
    def __init__(self, num_triangulos, num_vertices, vertices, triangulos, cor):

        self.num_triangulos = num_triangulos
        self.num_vertices = num_vertices
        self.vertices = vertices
        self.triangulos = triangulos
        self.cor = cor

    '''def intersect(self, raio: Raio):
        t = float('inf')

        for triangulo in self.triangulos:
            curr, id = triangulo.intersect(raio)
            if curr[0] >= 0:
                if curr[1] < t:
                    t = curr[0]
                    id = curr[1]

        return curr '''
