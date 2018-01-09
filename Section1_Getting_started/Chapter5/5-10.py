#! python3

current_users = ['Michel', 'Tom', 'Jane', 'Alice', 'Li Ming']
new_users = ['Michel', 'Jane', 'Lucy', 'Davaid', 'Bob']
new_current_users = [ current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower() not in new_current_users:
        print("This username can be used: %s" %(new_user))
    else:
        print("Occupied name: %s.  Please choose another name." %(new_user))
