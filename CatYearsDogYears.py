def animal_years(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5
    return [humanYears, catYears, dogYears]

# Pruebas
test_cases = [1, 2, 3, 5, 10]
results = [animal_years(humanYears) for humanYears in test_cases]
print(results)
