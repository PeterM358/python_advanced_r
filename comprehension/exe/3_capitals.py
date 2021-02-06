countries = input().split(", ")
capitals = input().split(", ")

result = {countries[index]: capitals[index] for index in range(len(countries))}
# for (city, capital) in result.items():
#     print(f'{city} -> {capital}')

print(*[f'{city} -> {capital}' for (city, capital) in result.items()], sep='\n')

result_1 = {country: capital for country, capital in tuple(zip(countries, capitals))}
[print(f"{country} -> {capital}") for country, capital in result_1.items()]
