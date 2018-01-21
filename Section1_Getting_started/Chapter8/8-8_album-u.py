#! python3

# define a function
def make_album(singer, album, w_nu=''):
    albums = {'singer': singer.title(), 'album': album.title()}
    if w_nu:
        albums['w_nu'] = w_nu
    return albums
while True:
    print('\nPlease show me your information about this.')
    print('\nEnter \'q\' to quit.')
    singer = input("Please input the singer's name:\n")
    if singer == 'q':
        break
    album = input("Please input the singer's album:\n")
    if album == 'q':
        break

    all_info = make_album(singer, album)
    print(all_info)
#
# a1 = make_album('tom', 'tom\'s album')
# a2 = make_album('jerry henter', 'JH-album')
# a3 = make_album('happer tofds', 'donnot know', 3)
# print(a1)
# print(a2)
# print(a3)