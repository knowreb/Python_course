# 9.13 Dice
class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        return randint(1, self.sides)

sides6 = Die()

results = []
for roll in range(10):
    result = sides6.roll_die()
    results.append(result)
print("10 rolls of a 6-sides die:")
print(results)

sides10 = Die()

results = []
for roll in range(10):
    result = sides10.roll_die()
    results.append(result)
print("10 rolls of a 10-sizes dies:")
print(results)

sides20 = Die()

results = []
for roll in range(10):
    result = sides20.roll_die()
    results.append(result)
print("10 rolls of a 20-sizes dies:")
print(results)

# 9.14 Lottery

from random import choice
lottery_numbers = [3, 6, 9, 2, 5, 8, 1, 4, 7, 10, 's', 'd', 'f', 'g']
win_ticket = []


print(f'Win ticket is: ')

while len(win_ticket) < 4:
    draw = choice(lottery_numbers)

    if draw not in win_ticket:
        print(f"We drawed a: {draw}")
        win_ticket.append(draw)

print(f"\nWin ticket is {win_ticket}")

# 9.15 Analysis of the lottery

from random import choice

while len(win_ticket) < 4:
    draw = choice(lottery_numbers)

    if draw not in win_ticket:
        print(f"We drawed a: {draw}")
        win_ticket.append(draw)

lottery_numbers = [3, 6, 9, 2, 5, 8, 1, 4, 7, 10, 'b', 'h', 'u', 'y']
my_numbers = ['b', 'u', 'h', 3]


drawn_numbers = []
iterations = 0

while my_numbers != drawn_numbers:
    drawn = choice(lottery_numbers)
    drawn_numbers.append(drawn)
    iterations +=1

print(f"Numbers on Your ticket: {my_numbers}")
print(f"Wylosowane liczby: {drawn_numbers}")
print(f"Liczba powtórzeń: {iterations}")
