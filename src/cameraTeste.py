from camera import Camera
import numpy as np

# Definir parâmetros da câmera
C = [0, 0, 0]  # Localização da câmera
M = [0, 0, -1]  # Ponto de mira
V_up = [0, 1, 0]  # Vetor apontando para cima
d = 1  # Distância da câmera à tela
v_res = 480  # Resolução vertical
h_res = 640  # Resolução horizontal

# Criar uma instância da câmera
camera = Camera(C, M, V_up, d, v_res, h_res)

# Testar métodos de atualização
nova_posicao = [1, 0, 0]
camera.atualizar_posicao(nova_posicao)
print("Nova posição da câmera:", camera.C)

novo_mira = [0, 1, -1]
camera.atualizar_ponto_mira(novo_mira)
print("Novo ponto de mira:", camera.M)

novo_vup = [0, 0, 1]
camera.atualizar_vetor_up(novo_vup)
print("Novo vetor up:", camera.V_up)

nova_distancia = 2
camera.atualizar_distancia_tela(nova_distancia)
print("Nova distância da câmera à tela:", camera.d)

nova_v_res = 720
nova_h_res = 1280
camera.atualizar_resolucao_tela(nova_v_res, nova_h_res)
print("Nova resolução vertical:", camera.v_res)
print("Nova resolução horizontal:", camera.h_res)

# Testar mapeamento de pixel
i = 320  # Coordenada horizontal do pixel
j = 240  # Coordenada vertical do pixel
pos_mundo = camera.mapear_pixel(i, j)
print("Posição no mundo para o pixel ({}, {}):".format(i, j), pos_mundo)
