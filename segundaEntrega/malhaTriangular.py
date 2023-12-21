import numpy as np, uuid
from primeiraEntrega.pontos import Ponto
from triangulo import Triangulo
from raio import Raio


class MalhaTriangular:
    def __init__(self, num_triangulos, num_vertices, lista_vertices, triplas, norm_triang, norm_vet, cor_rgb, ):
        """
        Args:
            num_triangulos (int): numero de triangulos
            num_vertices (int): numero de vertices
            lista_vertices (list[tuple[float, float, float]]): lista de triplas que correspondem as coordenadas dos vertices
            triplas (list[tuple[int, int, int]]): triplas de indices na lista 'vertices' que representam um triangulo
            norm_triang (list[Vetor]): lista com normais de triangulos (vetores)
            norm_vet (list[Vetor]): lista com normais dos vértices (vetor média das normais dos triângulos)
            cor_rgb (tuple[int, int, int]): cor RGB normalizada
        """
        self.num_triangulos = num_triangulos
        self.num_vertices = num_vertices
        # transforma a lista de triplas de coordenadas em uma lista de Pontos
        self.vertices = [(Ponto(vertice[0], vertice[1], vertice[2])) for vertice in lista_vertices]
        # lista de triangulos com os pontos correspondentes à lista de vértices de acordo com os indices de cada tripla
        # que representa um triangulo
        self.lista_triangulos = [Triangulo(pontos=(self.vertices[tripla[0]], self.vertices[tripla[1]],
                                                   self.vertices[tripla[2]]), cor=cor_rgb)
                                 for tripla in triplas]
        self.norm_triang = np.array(norm_triang)
        self.norm_vet = np.array(norm_vet)
        # self.cor_rgb = cor_rgb

    def intersect(self, raio: Raio):
        t = float('inf')
        id = -1

        for triangulo in self.lista_triangulos:
            curr, id = triangulo.intersect(raio)
            if curr[0] >= 0:
                if curr[1] < t:
                    t = curr[0]
                    id = curr[1]

        return curr
