import sympy as sp

# Definição das variáveis simbólicas
x, a, h = sp.symbols('x a h')

# Equações das curvas
y1 = h / a * x  # Reta: y = mx
y2 = h / a*2 * x*2  # Parábola: y = kx^2

# Cálculo da área da superfície
A = sp.integrate((y1 - y2), (x, 0, a))

# Cálculo da coordenada x do centróide (x̄)
x_centroid = sp.integrate(x * (y1 - y2), (x, 0, a)) / A

# Cálculo da coordenada y do centróide (ȳ)
y_centroid = sp.integrate((y1 + y2) / 2 * (y1 - y2), (x, 0, a)) / A

# Exibindo as expressões do centróide
x_centroid_simplified = sp.simplify(x_centroid)
y_centroid_simplified = sp.simplify(y_centroid)

print("Coordenada x do centróide (x̄):", x_centroid_simplified)
print("Coordenada y do centróide (ȳ):", y_centroid_simplified)