filename = 'guest_book.txt'

#待解决问题：只有退出循环时，才会将内容写入到文本中。

with open(filename, 'a') as file_object:

    while True:
        visitor_name = input("Please input your name:\n")
        if visitor_name != '':
            file_object.write(visitor_name.title() + '\n')
            print("It's my pleasure to have your name, %s\n" % visitor_name.title())
        else:
            break
"""

    while True:
        visitor_name = input("Please input your name:\n")
        if visitor_name == '':
            break
        else:
            print("It's my pleasure to have your name, %s" % visitor_name.title())
        file_object.write(visitor_name.title() + '\n')    
"""