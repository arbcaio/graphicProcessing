from primeiraEntrega.pontos import Ponto
from primeiraEntrega.vetor import Vetor


class Raio:
    def __init__(self, loc: Ponto, direcao: Vetor):
        self.loc = loc
        self.dir = direcao
