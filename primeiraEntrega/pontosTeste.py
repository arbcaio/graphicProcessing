from pontos import Ponto

# Criar pontos
ponto1 = Ponto(1, 2, 3)
ponto2 = Ponto(4, 5, 6)

# Testar operações sob pontos
soma = ponto1 + ponto2
subtracao = ponto1 - ponto2
multiplicacao = ponto1 * 2

# Imprimir resultados
print("Ponto 1:", ponto1)
print("Ponto 2:", ponto2)
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

# Testar distância entre pontos
distancia = ponto1.distancia_ate(ponto2)
print("Distância entre Ponto 1 e Ponto 2:", distancia)
