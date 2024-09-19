def dating_range(age):
    if age > 14:
        min_age = age // 2 + 7
        max_age = (age - 7) * 2
    else:
        min_age = int(age - 0.10 * age)
        max_age = int(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplo de uso
print(dating_range(27))  # Resultado: 20-40
print(dating_range(5))  # Resultado: 4-5
print(dating_range(17))  # Resultado: 15-20
