from sympy import symbols

def calcular_momento_inercia(b, h, t, d, a):
    # Área da figura externa
    area_externa = b * h

    # Área da abertura interna (retângulo mais triângulos)
    area_interna_retangulo = (b - 2 * t) * (h - 2 * t)
    area_interna_triangulos = 2 * (d * a / 2)
    area_interna = area_interna_retangulo + area_interna_triangulos

    # Área total
    area_total = area_externa - area_interna

    # Momento de inércia da figura externa em relação ao eixo centroidal
    I_externa = (b * (h ** 3)) / 12

    # Momento de inércia da abertura interna em relação ao eixo centroidal
    I_interna_retangulo = ((b - 2 * t) * ((h - 2 * t) ** 3)) / 12
    I_interna_triangulos = 2 * ((d * a ** 3) / 36)  # Triângulos em relação ao seu próprio eixo
    I_interna = I_interna_retangulo + I_interna_triangulos

    # Momento de inércia total
    I_total = I_externa - I_interna

    return I_total

# Definição simbólica das variáveis
b, h, t, d, a = symbols('b h t d a')

# Cálculo do momento de inércia
I_total = calcular_momento_inercia(b, h, t, d, a)
print(f"O momento de inércia da área em relação ao eixo centroidal paralelo à base é expresso como: {I_total}.")
