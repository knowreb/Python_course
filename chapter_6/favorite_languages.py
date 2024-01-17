# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
#     }
#
# language = favorite_languages['sara'].title()
# print(f"Ulubiony język programowania Sary to {language}.")
#
# for name, language in favorite_languages.items():
#     print(f"Ulubiony język programowania użytkownika {name.title()} to {language.title()}.")

#6.6 ankieta
favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
    }
dodatkowe_osoby = ['elżbieta', 'maria', 'józef']
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, dziękujemy za poświęcony czas i udział w ankiecie.')

if 'elżbieta' not in favorite_languages.keys():
    print("Elżbieta, proszę weź udział w naszej ankiecie!")

for name in dodatkowe_osoby:
    print(f'{name.title()}, proszę weź udział w ankiecie!')


favorite_languages = {
     'janek': ['python', 'ruby'],
     'sara': ['c'],
     'edward': ['ruby', 'go'],
     'paweł': ['python', 'haskell'],
     }

for name, languages in favorite_languages.items():
    print(f"\nUlubione języki programowania użytkownika {name.title()} to:")
    for language in languages:
        print(f"\t{language.title()}")
