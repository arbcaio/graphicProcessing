import numpy as np

class Vetor:
    def __init__(self, x, y, z=0):
        self.coordenadas = np.array([x, y, z])

    def __add__(self, outro):
        return Vetor(*(self.coordenadas + outro.coordenadas))

    def __sub__(self, outro):
        return Vetor(*(self.coordenadas - outro.coordenadas))

    def produto_escalar(self, outro):
        return np.dot(self.coordenadas, outro.coordenadas)

    def produto_vetorial(self, outro):
        return Vetor(*np.cross(self.coordenadas, outro.coordenadas))

    def norma(self):
        return np.linalg.norm(self.coordenadas)

    def normalizar(self):
        norma = self.norma()
        if norma == 0:
            raise ValueError("Não é possível normalizar o vetor zero.")
        return Vetor(*(self.coordenadas / norma))

    def __repr__(self):
        return f"Vetor({self.coordenadas[0]}, {self.coordenadas[1]}, {self.coordenadas[2]})"
