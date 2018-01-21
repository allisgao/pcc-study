#! python3

def build_person(fname, lname, age=''):
    person = {'first': fname, 'last': lname}
    if age:
        person['age'] = age
        return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)



