from intersecoes import Esfera, Plano, intersecao_raio_esfera, intersecao_raio_plano
import numpy as np

# Definir uma esfera
centro_esfera = [0, 0, 0]
raio_esfera = 1
cor_esfera = [255, 0, 0]  # Cor em formato RGB
esfera = Esfera(centro_esfera, raio_esfera, cor_esfera)

# Definir um plano
ponto_plano = [0, 0, -1]
vetor_normal_plano = [0, 0, 1]
cor_plano = [0, 0, 255]  # Cor em formato RGB
plano = Plano(ponto_plano, vetor_normal_plano, cor_plano)

# Definir origem e direção de um raio
origem_raio = [0, 0, -2]
direcao_raio = [0, 0, 1]

# Testar interseção entre raio e esfera
ponto_intersecao_esfera = intersecao_raio_esfera(origem_raio, direcao_raio, esfera)
if ponto_intersecao_esfera is not None:
    print("Interseção com a esfera:", ponto_intersecao_esfera)
else:
    print("Nenhuma interseção com a esfera")

# Testar interseção entre raio e plano
ponto_intersecao_plano = intersecao_raio_plano(origem_raio, direcao_raio, plano)
if ponto_intersecao_plano is not None:
    print("Interseção com o plano:", ponto_intersecao_plano)
else:
    print("Nenhuma interseção com o plano")
