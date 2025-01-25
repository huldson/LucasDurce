import math

def calcular_tracao(y, comprimento_fio, P):
    # Distâncias fornecidas no problema
    x_B = 200  # Distância horizontal entre o ponto fixo e o ponto B em mm
    comprimento_fio /= 1000  # Converter comprimento do fio para metros
    y /= 1000  # Converter y para metros
    x_B /= 1000  # Converter x_B para metros

    # Comprimento horizontal do fio entre os pontos A e B
    x_A = math.sqrt(comprimento_fio**2 - y**2)

    # Ângulo do fio com a horizontal
    theta = math.atan(y / x_A)

    # Tração no fio T (equilíbrio no ponto A)
    T = P / math.sin(theta)

    return T

def calcular_forca_Q(y, comprimento_fio, T):
    # Distâncias fornecidas no problema
    x_B = 200  # Distância horizontal entre o ponto fixo e o ponto B em mm
    comprimento_fio /= 1000  # Converter comprimento do fio para metros
    y /= 1000  # Converter y para metros
    x_B /= 1000  # Converter x_B para metros

    # Comprimento horizontal do fio entre os pontos A e B
    x_A = math.sqrt(comprimento_fio**2 - y**2)

    # Ângulo do fio com a horizontal
    theta = math.atan(y / x_A)

    # Componente horizontal da força Q (equilíbrio no ponto B)
    Q = T * math.cos(theta)

    return Q

# Parâmetros fornecidos no problema
comprimento_fio = 525  # mm
P = 341  # N
y = 155  # mm

# (a) Calcular a tração no fio quando y = 155 mm
T = calcular_tracao(y, comprimento_fio, P)
print(f"(a) A tração no fio é T = {T:.2f} N")

# (b) Calcular a força Q necessária para manter o equilíbrio
Q = calcular_forca_Q(y, comprimento_fio, T)
print(f"(b) A força Q necessária é Q = {Q:.2f} N")
