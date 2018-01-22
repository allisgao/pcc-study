#! python3

def make_great(magicians,g_magicians):
    while magicians:
        magician = magicians.pop()
        magician =  "The Great " + magician
        g_magicians.append(magician.title())

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['tom', 'jerry', 'job']
g_magicians = []
make_great(magicians[:],g_magicians)
show_magicians(g_magicians)
print("\nThe original list: ")
print(magicians)

