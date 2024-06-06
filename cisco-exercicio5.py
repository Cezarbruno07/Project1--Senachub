def liters_100km_to_miles_gallon(liters):
    return 235.215 / liters

def miles_gallon_to_liters_100km(miles):
    return 235.215 / miles

print(liters_100km_to_miles_gallon(3.9))  # Saída: aproximadamente 60.38
print(liters_100km_to_miles_gallon(7.5))  # Saída: aproximadamente 31.36
print(liters_100km_to_miles_gallon(10.0)) # Saída: 23.52
print(miles_gallon_to_liters_100km(60.3))  # Saída: aproximadamente 3.9
print(miles_gallon_to_liters_100km(31.4))  # Saída: aproximadamente 7.5
print(miles_gallon_to_liters_100km(23.5))  # Saída: 10.0
