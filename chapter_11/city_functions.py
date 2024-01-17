def city_country(city, country, population = 0):
    """generated name of city and country - population"""
    full_name = f"{city.title()}, {country.title()}"
    if population:
        full_name += f" - population {population}"
    return full_name
