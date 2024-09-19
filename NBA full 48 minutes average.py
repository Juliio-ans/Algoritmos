def points_per_48(ppg, mpg):
    if mpg == 0:  # Si el jugador no juega minutos, retorna 0
        return 0
    # Extrapola los puntos por 48 minutos
    return round(ppg * (48 / mpg), 1)

# Ejemplo de uso
print(points_per_48(25, 40))  # Resultado: 30.0
