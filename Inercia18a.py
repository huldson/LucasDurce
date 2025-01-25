import math

def calcular_momento_inercia():
    # Dimensões da figura (em metros)
    largura_base = 200 / 1000
    altura_base = 100 / 1000

    largura_parte_superior = 100 / 1000
    altura_parte_superior = 50 / 1000

    diametro_circulo = 60 / 1000
    raio_circulo = diametro_circulo / 2

    # Distância do centróide global ao eixo da base
    y_barra = 76.4 / 1000

    # Áreas das partes da figura
    area_base = largura_base * altura_base
    area_parte_superior = largura_parte_superior * altura_parte_superior
    area_circulo = math.pi * (raio_circulo ** 2)

    # Cálculo das posições dos centróides locais
    y_base = altura_base / 2
    y_parte_superior = altura_base + (altura_parte_superior / 2)
    y_circulo = altura_base + altura_parte_superior - raio_circulo

    # Momento de inércia das formas básicas em relação ao próprio eixo centroidal
    I_base = (largura_base * (altura_base ** 3)) / 12
    I_parte_superior = (largura_parte_superior * (altura_parte_superior ** 3)) / 12
    I_circulo = (math.pi * (raio_circulo ** 4)) / 4

    # Aplicação do teorema dos eixos paralelos
    d_base = abs(y_barra - y_base)
    d_parte_superior = abs(y_barra - y_parte_superior)
    d_circulo = abs(y_barra - y_circulo)

    I_total = (
        I_base + area_base * (d_base ** 2)
        + I_parte_superior + area_parte_superior * (d_parte_superior ** 2)
        - I_circulo - area_circulo * (d_circulo ** 2)
    )

    return I_total

# Resultado
momento_inercia = calcular_momento_inercia()
print(f"O momento de inércia da área em relação ao eixo centroidal paralelo à base é {momento_inercia:.6f} m^4.")