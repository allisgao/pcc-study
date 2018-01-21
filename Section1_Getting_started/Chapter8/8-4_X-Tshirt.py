#! python3

def make_shirt(size='X', sentense='I love Python'):
    print('\nThe size of this T-shirt is %s, and the sentense is \"%s\".' % (size, sentense))

make_shirt()
make_shirt(size='M')
make_shirt(sentense='I\' m the best!')