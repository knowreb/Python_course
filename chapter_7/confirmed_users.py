# Rozpoczynamy od uzytkownikow ktorzy maja byc zweryfikowani
# tworzymy tez pusta liste przeznaczona do przechowywania zweryfikowanych uzytkownikow
unconfirmed_users = ['alicja', 'bartek', 'katarzyna',]
confirmed_users = []

# weryfikujemy [pszczegolnych uzytkownikow, ddpoki lista nie bedzie pusta.
# kazdego zweryfikowanego uzytkownika przenosimy na oddzielna liste
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Weryfikacja użytkownika: {current_user.title()}")
    confirmed_users.append(current_user)

# wyświetlenie wszystkich zweryfikowanych uzytkownikow
print("\nZweryfikowano wymienionych poniżej użytkowników:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())