# page197 dictionary return
def build_person(first_name, last_name):
    """Returns a dictionery of information about person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

# with age
def build_person(first_name, last_name, age =None):
    """Returns a dictionery of information about person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix')
print(musician)