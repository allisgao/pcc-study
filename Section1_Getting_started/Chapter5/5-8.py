#! python3

users = ['tom', 'machile', 'admin', 'allis', 'jerry']

for user in users:
    if user == 'admin':
        print("Hello %s, would you like to see a status report?" %(user.title()))
    else:
        print("Hello %s, thank you for logging in again." % (user.title()))








