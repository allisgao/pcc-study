#! python3

# define a function
def make_album(singer, album, w_nu=''):
    albums = {'singer': singer.title(), 'album': album.title()}
    if w_nu:
        albums['w_nu'] = w_nu
    return albums

a1 = make_album('tom', 'tom\'s album')
a2 = make_album('jerry henter', 'JH-album')
a3 = make_album('happer tofds', 'donnot know', 3)
print(a1)
print(a2)
print(a3)