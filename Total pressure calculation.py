def total_pressure(M1, M2, m1, m2, V, T):
    # Constante de gas R en unidades: dm^3⋅atm⋅K^−1⋅mol^−1
    R = 0.082
    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15
    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V
    return P_total

# Ejemplo de uso
M1 = 2  # g/mol
M2 = 3  # g/mol
m1 = 4  # g
m2 = 5  # g
V = 10  # dm^3
T = 25  # °C

print(total_pressure(M1, M2, m1, m2, V, T))  # Resultado: presión total en atm
