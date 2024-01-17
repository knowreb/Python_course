print("2.3")
name = "adrian"
print(f"Hello {name.title()}! Do you want to learn Python?")

print("\n2.4")
name = "adrian"
print(name.lower())
print(name.upper())
print(name.title())

print("\n2.5")
name = "albert einstein"
print(f"{name.title()} once said: 'A person who has never made a mistake is someone who has never tried anything new.'")

print("\n2.6")
famous_person = "albert einstein"
message = "once said: 'A person who has never made a mistake is someone who has never tried anything new.'"
print(famous_person.title(), message)

print("\n2.7")
name = "\t Adrian Rock \n"
print("Basic:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip()")
print(name.strip())