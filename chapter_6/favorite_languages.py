favorite_languages = {
    'john': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'paul': 'python',
    }

language = favorite_languages['sara'].title()
print(f"{language}.")

for name, language in favorite_languages.items():
    print(f"User's favourite programming language {name.title()} to {language.title()}.")

#6.6 survey

favorite_languages = {
    'john': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'paul': 'python',
    }
additional_persons = ['elisabeth', 'marie', 'joseph']
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for your time and participation in the survey.')

if 'elisabeth' not in favorite_languages.keys():
    print("Elisabeth, please take part in our survey!")

for name in additional_persons:
    print(f'{name.title()}, please take part in the survey!')


favorite_languages = {
     'janek': ['python', 'ruby'],
     'sara': ['c'],
     'edward': ['ruby', 'go'],
     'paweł': ['python', 'haskell'],
     }

for name, languages in favorite_languages.items():
    print(f"\nUser favourite programming languages {name.title()} is:")
    for language in languages:
        print(f"\t{language.title()}")
