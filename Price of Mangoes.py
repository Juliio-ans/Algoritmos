def mango_cost(quantity, price_per_mango):
    # Por cada 3 mangos, solo se paga por 2
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)
    return paid_mangoes * price_per_mango

# Ejemplo de uso
print(mango_cost(7, 3))  # Resultado: 15
