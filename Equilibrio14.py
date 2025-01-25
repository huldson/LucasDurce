import math

def calcular_binario(theta_graus, forca, distancia_d, distancia_b):
    # Converte o ângulo para radianos
    theta = math.radians(theta_graus)

    # Calcula as componentes da força em D
    forca_vertical = forca * math.sin(theta)
    forca_horizontal = forca * math.cos(theta)

    # Determina o momento necessário para equilibrar o sistema
    # Momento M é gerado em torno do ponto A
    momento = forca_vertical * distancia_d - forca_horizontal * distancia_b

    return momento

# Dados do problema
angulo = 30  # em graus
forca_d = 150  # em N
distancia_d = 0.1  # em metros (100 mm convertido para metros)
distancia_b = 0.08  # em metros (80 mm convertido para metros)

# Calcula o momento
momento_necessario = calcular_binario(angulo, forca_d, distancia_d, distancia_b)

print(f"O binário necessário para manter o sistema em equilíbrio é M = {momento_necessario:.2f} N·m")
