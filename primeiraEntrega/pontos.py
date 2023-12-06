import numpy as np

class Ponto:
    def __init__(self, x, y, z=0):
        self.coordenadas = np.array([x, y, z])

    def __add__(self, outro):
        return Ponto(*(self.coordenadas + outro.coordenadas))

    def __sub__(self, outro):
        return Ponto(*(self.coordenadas - outro.coordenadas))

    def __mul__(self, escalar):
        return Ponto(*(self.coordenadas * escalar))

    def __repr__(self):
        return f"Ponto({self.coordenadas[0]}, {self.coordenadas[1]}, {self.coordenadas[2]})"

    def distancia_ate(self, outro):
        return np.linalg.norm(self.coordenadas - outro.coordenadas)
