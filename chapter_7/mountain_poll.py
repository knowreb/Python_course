responses = {}

# ustawienie flagi wskazujacej, czy ankieta jest aktywna
polling_active = True
while polling_active:
    # prośba o podanie imienia uczestnika ankiety oraz odpowiedzi na pytanie.
    name = input("\nJak masz na imię?")
    response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia?")

    # umieszczenie odpowiedzi w słowniku:
    responses[name] = response
    # ustalenie czy ktokolwiek jeszcze chce wziać udział w ankiecie.
    repeat = input("Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie)")
    if repeat == 'nie':
        polling_active = False

# ankieta została zakończona i wyświetlamy jej wyniki.
print("\n--- Wyniki ankiety ---")
for name, response in responses.items():
    print(f"{name} chciałby się wspiąć na {response}.")