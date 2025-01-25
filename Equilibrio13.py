import numpy as np

def calcular_tracoes_e_reacoes(forca_c, pos_c, pos_b, pos_d, pos_e, pos_a):
    # Vetores posição dos cabos em relação a B
    r_bd = pos_d - pos_b
    r_be = pos_e - pos_b
    r_bc = pos_c - pos_b

    # Normalizando os vetores direção dos cabos
    u_bd = r_bd / np.linalg.norm(r_bd)
    u_be = r_be / np.linalg.norm(r_be)
    u_bc = r_bc / np.linalg.norm(r_bc)

    # Montagem da matriz de equilíbrio
    # As três equações de equilíbrio são baseadas em ∑F = 0
    matriz_equilibrio = np.array([
        u_bd,  # Direção do cabo BD
        u_be,  # Direção do cabo BE
        [1, 0, 0],  # Reação em A na direção x
    ]).T

    # Vetor força resultante (inclui a força aplicada e ∑F em A)
    forca_resultante = np.array([-forca_c[0], -forca_c[1], -forca_c[2]])

    # Resolvendo o sistema linear
    tracoes_reacoes = np.linalg.solve(matriz_equilibrio, forca_resultante)

    # Resultados
    trac_bd = tracoes_reacoes[0]  # Tração no cabo BD
    trac_be = tracoes_reacoes[1]  # Tração no cabo BE
    reacao_a = tracoes_reacoes[2]  # Reação em A

    return trac_bd, trac_be, reacao_a

# Dados do problema
forca_c = np.array([0, 0, -455])  # Força aplicada no ponto C, em N
pos_c = np.array([0, 0, 6])  # Posição do ponto C, em metros
pos_b = np.array([0, 0, 3])  # Posição do ponto B, em metros
pos_d = np.array([1.5, 1.5, 0])  # Posição do ponto D, em metros
pos_e = np.array([-1.5, 1.5, 0])  # Posição do ponto E, em metros

# Input para o valor de a
a = float(input("Digite o valor de a (em metros): "))
pos_a = np.array([0, -a, 0])  # Posição do ponto A varia com a

# Cálculo das trações e reações
trac_bd, trac_be, reacao_a = calcular_tracoes_e_reacoes(forca_c, pos_c, pos_b, pos_d, pos_e, pos_a)

print(f"\nPara a = {a} m:")
print(f"Tração no cabo BD: {trac_bd:.2f} N")
print(f"Tração no cabo BE: {trac_be:.2f} N")
print(f"Reação em A: {reacao_a:.2f} N")
