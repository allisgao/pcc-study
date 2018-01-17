#! python3
rivers = {'nile':'egypt', 'yellow-river':'china', 'times':
          'france'}
# print a msg for each river
for k,v in rivers.items():
    print("The %s runs through %s" % (k.title(),v.title()))
# use loop to print all river names
print('\n')
for rname in rivers:
    print(rname.title())
print("\n")
for cname in rivers.values():
    print(cname.title())
# use loop to print all countries


