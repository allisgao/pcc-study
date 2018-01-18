#! python3
dreamlands = {}
active_status = True

while active_status:
    name = input("What's your name?\n")
    dreamland = input("What's your dreamland?\n")
    dreamlands[name] = dreamland
    repeat = input("Continue?(yes/no)\n")
    if repeat == 'no':
        active_status = False

print("\n----- Poll Results -----")
for name, dreamland in dreamlands.items():
    print("%s's dreamland is %s." % (name.title(), dreamland.title()))
