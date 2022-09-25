person_0 = {'first_name': 'mary', 'last_name': 'barry', 'age': 17,
'city': 'new york'}
person_1 = {'first_name': 'stephen', 'last_name': 'hawkings', 'age': 30,
'city': 'palestine'}
person_2 = {'first_name': 'nikola', 'last_name': 'tesla', 'age': 40,
'city': 'egypt'}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tLocation(city): {person['city'].title()}\n")