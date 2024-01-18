# using the break command to leave the loop
prompt = "\nName the cities you would like to visit:"
prompt += "\n(When you have finished naming the cities, write 'end'). "

while True:
    city = input(prompt)

    if city == 'end':
        break
    else:
        print(f"I would like to visit {city.title()}!")
