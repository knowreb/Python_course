# We start with the users to be verified
# We also create an empty list to hold verified users
unconfirmed_users = ['alice', 'bart', 'kate',]
confirmed_users = []

# we verify individual users so that the list is not empty.
# we move each verified user to a separate list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"User verification: {current_user.title()}")
    confirmed_users.append(current_user)

# display of all verified users
print("\nThe following users were verified:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
