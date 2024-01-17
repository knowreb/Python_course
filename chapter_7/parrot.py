message = input("Powiedz mi coś o sobie, a wyświetlę to na ekranie: ")
print(message)

# petla while
prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie:"
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "
message = ""
while message != 'koniec':
    message = input(prompt)
    if message != 'koniec':
        print(message)

# dodanie flagi
prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie:"
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

active = True
while active:
    message = input(prompt)

    if message == 'koniec':
        active = False
    else:
        print(message)