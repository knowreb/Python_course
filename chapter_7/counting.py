# displaying numbers from 1 to 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

# using the continue command in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# avoiding the loop running indefinitely
x=1
while x <= 5:
    print(x)
    x += 1
