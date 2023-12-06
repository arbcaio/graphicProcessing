import numpy as np

class Camera:
    def __init__(self, C, M, V_up, d, v_res, h_res):
        self.C = np.array(C)  # Localização da Câmera
        self.M = np.array(M)  # Ponto de Mira
        self.V_up = np.array(V_up)  # Vetor Apontando para Cima

        self.d = d  # Distância da Câmera à Tela
        self.v_res = v_res  # Resolução Vertical
        self.h_res = h_res  # Resolução Horizontal

        self._calcular_vetores_base()

    def _calcular_vetores_base(self):
        # Calcula os vetores ortonormais
        W = (self.C - self.M) / np.linalg.norm(self.C - self.M)  # Normalizado
        U = np.cross(self.V_up, W)
        U /= np.linalg.norm(U)  # Normalizado
        V = np.cross(W, U)

        self.W = W
        self.U = U
        self.V = V

    def atualizar_posicao(self, nova_posicao):
        self.C = np.array(nova_posicao)
        self._calcular_vetores_base()

    def atualizar_ponto_mira(self, novo_mira):
        self.M = np.array(novo_mira)
        self._calcular_vetores_base()

    def atualizar_vetor_up(self, novo_vup):
        self.V_up = np.array(novo_vup)
        self._calcular_vetores_base()

    def atualizar_distancia_tela(self, nova_distancia):
        self.d = nova_distancia

    def atualizar_resolucao_tela(self, nova_v_res, nova_h_res):
        self.v_res = nova_v_res
        self.h_res = nova_h_res

    def mapear_pixel(self, i, j):
        # i e j são as coordenadas do pixel na tela

        # Normalizar as coordenadas do pixel
        u = (i - self.h_res / 2) / (self.h_res / 2) * self.d
        v = (j - self.v_res / 2) / (self.v_res / 2) * self.d

        # Calcular a posição no mundo
        pos_mundo = self.C + self.W * (-self.d) + self.U * u + self.V * v
        return pos_mundo