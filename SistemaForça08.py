import math

def calcular_momento_equivalente(m1, m2, direcao_m1, direcao_m2):
    """
    Calcula o momento resultante equivalente dado dois momentos vetoriais.

    Parâmetros:
    - m1: Magnitude do momento 1 (lb·ft).
    - m2: Magnitude do momento 2 (lb·ft).
    - direcao_m1: Direção do momento 1 em relação aos eixos (vetor [x, y, z]).
    - direcao_m2: Direção do momento 2 em relação aos eixos (vetor [x, y, z]).

    Retorna:
    - magnitude: Magnitude do momento resultante (lb·ft).
    - direcao: Vetor direção do momento resultante (normalizado).
    """
    # Componentes dos momentos
    mx = m1 * direcao_m1[0] + m2 * direcao_m2[0]
    my = m1 * direcao_m1[1] + m2 * direcao_m2[1]
    mz = m1 * direcao_m1[2] + m2 * direcao_m2[2]

    # Magnitude do momento resultante
    magnitude = math.sqrt(mx**2 + my**2 + mz**2)

    # Direção normalizada
    direcao = [mx / magnitude, my / magnitude, mz / magnitude]

    return magnitude, direcao

# Dados do problema
m1 = 15  # Magnitude do momento M1 (lb·ft)
m2 = 3   # Magnitude do momento M2 (lb·ft)

direcao_m1 = [1, 0, 0]  # Momento M1 no eixo x

direcao_m2 = [0, 1, 0]  # Momento M2 no eixo y

# Cálculo do momento equivalente
magnitude, direcao = calcular_momento_equivalente(m1, m2, direcao_m1, direcao_m2)

# Exibir os resultados
print(f"Magnitude do momento resultante: {magnitude:.2f} lb·ft")
print(f"Direção do momento resultante: [{direcao[0]:.2f}, {direcao[1]:.2f}, {direcao[2]:.2f}]")