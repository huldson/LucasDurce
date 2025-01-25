import math

# Dados em milímetros

M = 12  # Momento em N·m
dAB_mm = 450  # Distância entre A e B em mm
dBC_mm = 240  # Distância entre B e C em mm

# Calculando a distância entre A e C usando Pitágoras
dAC_mm = math.sqrt(dAB_mm*dAB_mm + dBC_mm*dBC_mm) # Distância entre A e C

# Convertendo milímetros para metros
dAB = dAB_mm / 1000  # Distância entre A e B em metros
dBC = dBC_mm / 1000  # Distância entre B e C em metros
dAC = dAC_mm /1000  # Distância entre A e C em metros



# Forças calculadas para cada caso
FA_FB = M / dAB  # Forças em A e B
FB_FC = M / dBC  # Forças em B e C
FA_FC = M / dAC  # Forças em A e C

# Exibindo os resultados
print("Forças calculadas:")
print(f"FA e FB (caso a): {FA_FB:.2f} N")
print(f"FB e FC (caso b): {FB_FC:.2f} N")
print(f"FA e FC (caso c): {FA_FC:.2f} N")