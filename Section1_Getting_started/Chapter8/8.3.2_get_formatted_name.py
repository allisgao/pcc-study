#! python3

def get_formatted_name(firstname, lastname, middlename=''):
    if middlename:
        full_name = firstname + ' ' + middlename + ' ' + lastname
    else:
        full_name = firstname + ' ' + lastname
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician + '\n')
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)