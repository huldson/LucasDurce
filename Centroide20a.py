from sympy import symbols, integrate

def calcular_centroide(a, h):
    # Definindo as variáveis simbólicas
    x, y = symbols('x y')

    # A equação da linha inclinada do triângulo (y = (h/a) * x)
    linha = (h / a) * x

    # Área do triângulo (base * altura / 2)
    area = (a * h) / 2

    # Coordenada x do centróide: (1/Área) * Integral[x * y dx]
    x_c = (1 / area) * integrate(x * linha, (x, 0, a))

    # Coordenada y do centróide: (1/Área) * Integral[(1/2) * y^2 dx]
    y_c = (1 / area) * integrate((1 / 2) * linha**2, (x, 0, a))

    return x_c, y_c

# Definindo as variáveis simbólicas a e h
a, h = symbols('a h')

# Calculando o centróide
x_c, y_c = calcular_centroide(a, h)

print(f"O centróide do triângulo em termos de a e h é dado por:")
print(f"x_c = {x_c}")
print(f"y_c = {y_c}")