# użycie polecenia break do opuszczenia petli
prompt = "\nPodaj nazwy miast, które chciałbyś odwiedzić:"
prompt += "\n(Gdy zakonczysz podawanie miast, napisz 'koniec'. "

while True:
    city = input(prompt)

    if city == 'koniec':
        break
    else:
        print(f"Chciałbym odwiedzić {city.title()}!")