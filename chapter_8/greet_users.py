def greet_users(names):
    """Displays a simple greeting to each user on the list"""
    for name in names:
        msg = f"Welcome, {name.title()}!"
        print(msg)

usernames = ['Jim', 'Alice', 'Kate']
greet_users(usernames)