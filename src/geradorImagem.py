from PIL import Image
import numpy as np

from camera import Camera
from intersecoes import Esfera, Plano, intersecao_raio_esfera, intersecao_raio_plano

def ler_arquivo_txt(nome_arquivo):
    cenas = {}
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        partes = linha.strip().split()
        if partes[0] == "Camera":
            # Exemplo: Camera 0 0 0 1 0 0 0 1 0 1 800 600
            cenas['camera'] = {
                'C': np.array([float(partes[1]), float(partes[2]), float(partes[3])]),
                'M': np.array([float(partes[4]), float(partes[5]), float(partes[6])]),
                'V_up': np.array([float(partes[7]), float(partes[8]), float(partes[9])]),
                'd': float(partes[10]),
                'v_res': int(partes[11]),
                'h_res': int(partes[12])
            }
        elif partes[0] == "Esfera":
            # Exemplo: Esfera 1 1 1 2 255 0 0
            if 'esferas' not in cenas:
                cenas['esferas'] = []
            cenas['esferas'].append({
                'centro': np.array([float(partes[1]), float(partes[2]), float(partes[3])]),
                'raio': float(partes[4]),
                'cor_rgb': np.array([int(partes[5]), int(partes[6]), int(partes[7])])
            })
        elif partes[0] == "Plano":
            # Exemplo: Plano 0 0 1 0 1 0 0 255 0
            if 'planos' not in cenas:
                cenas['planos'] = []
            cenas['planos'].append({
                'ponto': np.array([float(partes[1]), float(partes[2]), float(partes[3])]),
                'vetor_normal': np.array([float(partes[4]), float(partes[5]), float(partes[6])]),
                'cor_rgb': np.array([int(partes[7]), int(partes[8]), int(partes[9])])
            })
        # Adicione outras estruturas conforme necessário

    return cenas

def renderizar_cena(info_cena):
    # Criação da câmera com os dados do arquivo
    dados_camera = info_cena['camera']
    camera = Camera(dados_camera['C'], dados_camera['M'], dados_camera['V_up'], 
                    dados_camera['d'], dados_camera['v_res'], dados_camera['h_res'])

    # Criação de objetos na cena
    objetos = []
    if 'esferas' in info_cena:
        for esfera_info in info_cena['esferas']:
            objetos.append(Esfera(esfera_info['centro'], esfera_info['raio'], esfera_info['cor_rgb']))
    if 'planos' in info_cena:
        for plano_info in info_cena['planos']:
            objetos.append(Plano(plano_info['ponto'], plano_info['vetor_normal'], plano_info['cor_rgb']))

    # Inicialização da imagem
    imagem = np.zeros((camera.v_res, camera.h_res, 3), dtype=np.uint8)

    for i in range(camera.v_res):
        for j in range(camera.h_res):
            # Calcula a direção do raio para cada pixel
            direcao_raio = camera.mapear_pixel(i, j)

            cor_pixel = np.array([0, 0, 0])  # Cor padrão (preto)
            for objeto in objetos:
                intersecao = None
                # Verifica se há interseção do raio com o objeto
                if isinstance(objeto, Esfera):
                    intersecao = intersecao_raio_esfera(camera.C, direcao_raio, objeto)
                elif isinstance(objeto, Plano):
                    intersecao = intersecao_raio_plano(camera.C, direcao_raio, objeto)

                if intersecao is not None:
                    cor_pixel = objeto.cor_rgb
                    break  # Assumindo que o primeiro objeto interceptado determina a cor

            imagem[i, j] = cor_pixel
    dados_imagem = []
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            pixel = tuple(imagem[i, j])
            dados_imagem.append(pixel)

    return dados_imagem, (camera.h_res, camera.v_res)

def criar_imagem_ppm(dados_imagem, resolucao):
    img = Image.new('RGB', resolucao)
    img.putdata(dados_imagem)
    return img

def main():
    info_cena = ler_arquivo_txt('src\\cena.txt')
    dados_imagem, resolucao = renderizar_cena(info_cena)
    imagem = criar_imagem_ppm(dados_imagem, resolucao)
    imagem.save('saida.ppm')

if __name__ == "__main__":
    main()