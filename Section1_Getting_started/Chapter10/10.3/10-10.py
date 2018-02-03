#! python3

filename = "Hamlet.txt"

with open(filename, encoding='utf8') as f_obj:
    content = f_obj.read()

the_nu = content.lower().count("the")

print(str(the_nu))




