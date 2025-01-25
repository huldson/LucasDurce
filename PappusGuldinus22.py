import math

# Densidade do alumínio (kg/m³)
densidade = 2800

# Espessura da peça (m)
espessura = 1e-3

# Dimensões externas (m)
raio_maior_externo = 66e-3 / 2
raio_menor_externo = 56e-3 / 2
altura_externa_cilindro_maior = 32e-3
altura_externa_cilindro_menor = 26e-3
altura_total_externa = altura_externa_cilindro_maior + altura_externa_cilindro_menor

# Dimensões internas (m)
raio_maior_interno = raio_maior_externo - espessura
raio_menor_interno = raio_menor_externo - espessura

# Volume externo
volume_externo_cilindro_maior = math.pi * (raio_maior_externo**2) * altura_externa_cilindro_maior
volume_externo_cilindro_menor = math.pi * (raio_menor_externo**2) * altura_externa_cilindro_menor
volume_externo_total = volume_externo_cilindro_maior + volume_externo_cilindro_menor

# Volume interno
volume_interno_cilindro_maior = math.pi * (raio_maior_interno**2) * altura_externa_cilindro_maior
volume_interno_cilindro_menor = math.pi * (raio_menor_interno**2) * altura_externa_cilindro_menor
volume_interno_total = volume_interno_cilindro_maior + volume_interno_cilindro_menor

# Volume da peça
volume_peca = volume_externo_total - volume_interno_total

# Massa da peça
massa = volume_peca * densidade

# Exibir resultado
print(f"A massa da peça é {massa:.4f} kg")
