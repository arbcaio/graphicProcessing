from vetor import Vetor
import numpy as np

# Criar vetores
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(4, 5, 6)

# Testar operações com vetores
soma = vetor1 + vetor2
subtracao = vetor1 - vetor2
produto_escalar = vetor1.produto_escalar(vetor2)
produto_vetorial = vetor1.produto_vetorial(vetor2)
norma_vetor1 = vetor1.norma()
vetor_normalizado = vetor1.normalizar()

# Imprimir resultados
print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Soma:", soma)
print("Subtração:", subtracao)
print("Produto Escalar:", produto_escalar)
print("Produto Vetorial:", produto_vetorial)
print("Norma de Vetor 1:", norma_vetor1)
print("Vetor Normalizado:", vetor_normalizado)
