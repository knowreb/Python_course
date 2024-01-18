message = input("Tell me something about yourself and I will display it on the screen: ")
print(message)

# while loop
prompt = "\nTell me something about yourself and I will display it on the screen:"
prompt += "\nWrite 'end' to end the programme. "
message = ""
while message != 'end':
    message = input(prompt)
    if message != 'end':
        print(message)

# addition of a flag
prompt = "\nTell me something about yourself and I will display it on the screen:"
prompt += "\nWrite 'end' to end the programme. "

active = True
while active:
    message = input(prompt)

    if message == 'end':
        active = False
    else:
        print(message)
