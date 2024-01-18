users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'maria',
        'last': 'skłodowska-curie',
        'location': 'paris'
        }
    }
for username, user_info in users.items():
    print(f"\nUser name: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tName and last name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
