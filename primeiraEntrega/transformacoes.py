import numpy as np

def translacao(pontos, vetor_translacao):

    matriz_translacao = np.array([
        [1, 0, 0, vetor_translacao[0]],
        [0, 1, 0, vetor_translacao[1]],
        [0, 0, 1, vetor_translacao[2]],
        [0, 0, 0, 1]
    ])
    pontos_homogeneos = np.hstack((np.array(pontos), np.ones((len(pontos), 1))))
    pontos_transladados = np.dot(pontos_homogeneos, matriz_translacao.T)
    return pontos_transladados[:, :3].tolist()

def rotacao_x(pontos, angulo):

    angulo_radianos = np.radians(angulo)
    matriz_rotacao = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angulo_radianos), -np.sin(angulo_radianos), 0],
        [0, np.sin(angulo_radianos), np.cos(angulo_radianos), 0],
        [0, 0, 0, 1]
    ])
    pontos_homogeneos = np.hstack((np.array(pontos), np.ones((len(pontos), 1))))
    pontos_rotacionados = np.dot(pontos_homogeneos, matriz_rotacao.T)
    return pontos_rotacionados[:, :3].tolist()

def rotacao_y(pontos, angulo):

    angulo_radianos = np.radians(angulo)
    matriz_rotacao = np.array([
        [np.cos(angulo_radianos), 0, np.sin(angulo_radianos), 0],
        [0, 1, 0, 0],
        [-np.sin(angulo_radianos), 0, np.cos(angulo_radianos), 0],
        [0, 0, 0, 1]
    ])
    pontos_homogeneos = np.hstack((np.array(pontos), np.ones((len(pontos), 1))))
    pontos_rotacionados = np.dot(pontos_homogeneos, matriz_rotacao.T)
    return pontos_rotacionados[:, :3].tolist()

def rotacao_z(pontos, angulo):

    angulo_radianos = np.radians(angulo)
    matriz_rotacao = np.array([
        [np.cos(angulo_radianos), -np.sin(angulo_radianos), 0, 0],
        [np.sin(angulo_radianos), np.cos(angulo_radianos), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    pontos_homogeneos = np.hstack((np.array(pontos), np.ones((len(pontos), 1))))
    pontos_rotacionados = np.dot(pontos_homogeneos, matriz_rotacao.T)
    return pontos_rotacionados[:, :3].tolist()
