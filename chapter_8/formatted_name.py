def get_formatted_name(first_name, last_name):
    """Returns elegantly formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)