def make_country(country: str, capital: str) -> dict:
    country_capital = {country: capital}
    return country_capital

print(make_country("Ukraine", "Kyiv"))