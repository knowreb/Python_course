# wyswietlenie liczb od 1 do 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

# uzycie polecenia continue w petli
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# unikanie petli dzialajacej w nieskonczonosc
x=1
while x <= 5:
    print(x)
    x += 1
