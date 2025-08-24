celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
high_temps = list(filter(lambda f: f > 100, fahrenheit))
print("Temperatures in Fahrenheit:", fahrenheit)
print("Temperatures above 100°F:", high_temps)