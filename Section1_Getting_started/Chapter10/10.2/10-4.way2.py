#! python3
#待解决问题：只有退出循环时，才会将内容写入到文本中。

filename = 'guest_book.txt'

f = open(filename, 'a')

while True:
    f = open(filename, 'a')
    visitor_name = input("Please enter your name.\nPress ENTER to exit.\n")
    if visitor_name != '':
        print("It's my pleasure to have your name, %s" % visitor_name.title())
        f.write(visitor_name.title() + '\n')
        f.close()
    else:
        break