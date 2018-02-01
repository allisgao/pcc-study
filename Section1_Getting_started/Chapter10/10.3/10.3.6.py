#! python3

filename = "Alice.txt"

try:
    with  open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # calculate the number of this article
    words = contents.split()
    num_words = len(words)
    print("The file '%s' has about %s words." % (filename, str(num_words)))




