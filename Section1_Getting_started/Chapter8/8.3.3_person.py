#! python3

def build_person(first_name, last_name):
    '''return a dictionary,which contains a person's informaton.'''
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


