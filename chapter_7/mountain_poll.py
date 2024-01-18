responses = {}

# setting a flag to indicate whether a poll is active
polling_active = True
while polling_active:
    # requesting the name of the survey participant and the answer to the question.
    name = input("\nWhat is your name?")
    response = input("Which peak would you like to climb one day?")

    # putting the answer in the dictionary:
    responses[name] = response
    # finding out if anyone else wants to take part in the survey.
    repeat = input("Does anyone else want to take part in the survey? (yes / no)")
    if repeat == 'no':
        polling_active = False

# the survey has been completed and the results are displayed.
print("\n--- Survey results ---")
for name, response in responses.items():
    print(f"{name} would like to climb the {response}.")
