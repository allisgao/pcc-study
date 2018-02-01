# coding=utf-8

def count_words(filename):
    """ calculate how many words a text-file has"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file '" + filename + "' does not exist."
        print(msg)
    else:
        # calculate
        words = contents.split()
        num_words = len(words)
        print("The file '%s' has about %s words." % (filename, str(num_words)))


#filename = 'alice.txt'
filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt', 'not_exist.txt']
for filename in filenames:
    count_words(filename)
