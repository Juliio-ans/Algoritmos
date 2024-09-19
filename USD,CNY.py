def usd_to_cny(usd):
    conversion_rate = 6.75  # Ejemplo de tasa de conversión (USD a CNY)
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
print(usd_to_cny(100))  # Para 100 USD
