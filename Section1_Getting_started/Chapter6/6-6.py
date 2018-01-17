#! python3

flang = {
    "tom": "python",
    "jane": "ruby",
    "Alice": "java",
    "jerry": "c#"
}

names = ["tom", "jane", "mario", "bob", "davad"]

for name in flang:
    print("Thank you %s for research." % (name.title()))
for lname in names:
    if lname not in flang:
        print("We want to invite you %s to have this research." % (lname))


