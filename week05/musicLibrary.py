class Song:
    def __init__(self, artist, title, album, length):
        self.artist = artist
        self.title = title
        self.album = album
        self.song_length = length

    def __str__(self):
        return '{} - {} from {} - {}'.format(self.artist, self.title, self.album, self.song_length)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.artist, self.album, self.title, self.song_length) == (other.artist, other.album, other.title, other.song_length)
        return NotImplemented

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.artist, self.album, self.title, self.song_length))

    def length(self, seconds=False, minutes=False, hours=False):
        temp = self.song_length.split(':')[::-1]
        list_h_m_s = temp if len(temp) is 3 else temp + ['0']
        if seconds:
            return repr(int(list_h_m_s[2])*60**2 + int(list_h_m_s[1])*60 + int(list_h_m_s[0]))
        return self.song_length
   

class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.songs = []
        self.repeat = repeat
        self.shuffle = shuffle

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            print('{} already in playlist. '.format(song))

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print('Song was removed successfully')
        else:
            print('No such song in the playlst')

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def pprint_playlist(self):
        if len(self.songs) == 0:
            print('Empty playlist')
            return
        max_len_artist = max(max(len(song.artist) for song in self.songs), len('Artist'))
        max_len_length = max(max(len(song.song_length) for song in self.songs), len('Length'))
        max_len_title = max(max(len(song.title) for song in self.songs), len('Song'))
        print('| Artist', ' '*(max_len_artist - len('artist')), '| Song', ' '*(max_len_title - len('Song')), '| Length', ' '*(max_len_length - len('Length')), '|')
        print('|', '-'*(max_len_artist + 1), '|', '-'*(max_len_title + 1), '|', '-'*max_len_length + '-', '|')
        for song in self.songs:
            print('| {}'.format(song.artist), ' '*(max_len_artist - len(song.artist)), '| {}'.format(song.title), ' '*(max_len_title - len(song.title)), '| {}'.format(song.song_length), ' '*(max_len_length - len(song.song_length)), '|')
        print('\n')
    

if __name__ == '__main__':
    'in musicLibrary'
    s2 = Song('art', 't', 'a', length='3:00')
    s = Song('a', 't', 'a', length='3:30')
    print([s,s2])
    pl = Playlist('name')
    pl.add_song(s)
    pl.add_songs([s2,s,s,s])
    pl.pprint_playlist()
    pl.remove_song(s)
    pl.pprint_playlist()
    pl.remove_song(s)