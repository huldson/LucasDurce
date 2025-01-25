import numpy as np

# Densidades dos materiais (kg/m³)
rho1 = 2700
rho2 = 5700
rho3 = 7800

# Dimensões dos componentes (m)
# Componente 1 (prisma triangular)
base1 = 0.02  # largura da base
altura1 = 0.03  # altura do triângulo
profundidade1 = 0.06  # profundidade do prisma

# Componente 2 (prisma retangular)
largura2 = 0.02
altura2 = 0.04
profundidade2 = 0.06

# Componente 3 (prisma retangular)
largura3 = 0.06
altura3 = 0.02
profundidade3 = 0.06

# Volumes dos componentes
V1 = 0.5 * base1 * altura1 * profundidade1  # volume do prisma triangular
V2 = largura2 * altura2 * profundidade2  # volume do prisma retangular
V3 = largura3 * altura3 * profundidade3  # volume do prisma retangular

# Massas dos componentes
m1 = rho1 * V1
m2 = rho2 * V2
m3 = rho3 * V3

# Coordenadas do centro de massa de cada componente
# Componente 1: centro geométrico do prisma triangular
x1 = 0.01  # metade da largura da base
y1 = 0.06 + (altura1 / 3)  # 1/3 da altura do triângulo acima da base
z1 = profundidade1 / 2

# Componente 2: centro geométrico do prisma retangular
x2 = 0.01
y2 = 0.06 + altura2 / 2
z2 = profundidade2 / 2

# Componente 3: centro geométrico do prisma retangular
x3 = largura3 / 2
y3 = altura3 / 2
z3 = profundidade3 / 2

# Coordenadas do centro de massa do sistema
x_cm = (m1 * x1 + m2 * x2 + m3 * x3) / (m1 + m2 + m3)
y_cm = (m1 * y1 + m2 * y2 + m3 * y3) / (m1 + m2 + m3)
z_cm = (m1 * z1 + m2 * z2 + m3 * z3) / (m1 + m2 + m3)

# Resultado
print(f"Centro de massa do bloco:")
print(f"x_cm = {x_cm:.4f} m")
print(f"y_cm = {y_cm:.4f} m")
print(f"z_cm = {z_cm:.4f} m")
