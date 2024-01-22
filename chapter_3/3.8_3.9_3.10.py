print("3.8")
places = ['Norway', 'Iceland', 'Australia', 'New Zealand', 'USA']
print(places)

print(sorted(places))
print(places)

print(sorted(places, reverse=True))
print(places)

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

print("\n3.9")
visitors = ['Mary', 'Jane', 'Roma', 'Adrian']
print(len(visitors))

print("\n3.10")
country = ['Australia', 'Norway', 'Spain', 'Chile']
print(country[0])
print(country[1].title())
message = f"First of all, I would like to see {country[1].title()}!"
print(message)
country[2] = 'Brazil'
print(country)
country.append('Argentina')
print(country)
country.insert(0, 'USA')
print(country)
del country[1]
print(country)
pop_country = country.pop(0)
print(f"I think visit in {pop_country} could be the best!")
country.remove('Argentina')
print(country)
country.sort()
print(country)
country.sort(reverse=True)
print(country)
country.reverse()
print(country)
