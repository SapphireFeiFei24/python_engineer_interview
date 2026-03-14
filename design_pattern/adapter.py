'''
Definition
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of incompatible interfaces

Advantage:
Make the code compatible without changing existing code

Disadvantage:
Potential overhead and increased complexity

Let’s imagine a scenario where you have a system that requires
media players to play different types of media files (MP3, MP4),
but one of the existing media players only supports MP4 format.

You can use the Adapter Pattern to adapt the MP3Player to the interface
that the system expects, so that the player can be used in the system even though
 it doesn't directly support the format.
'''

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

class MP3Player:
    def play_mp3(self, filename):
        return f"Playing MP3:{filename}"

class MP4Player:
    def play(self, filename):
        return f"Playing MP4:{filename}"

class MP3Adapter(MediaPlayer):
    def __init__(self, mp3_player):
        self.player = mp3_player

    def play(self, filename):
        return self.player.play_mp3(filename)

def play_media(player, filename: str):
    print(player.play(filename))

if __name__ == "__main__":
    mp4_player = MP4Player()
    mp3_player = MP3Player()

    # Adapter used to make MP3Player compatible with MediaPlayer interface
    mp3_adapter = MP3Adapter(mp3_player)

    # Playing media files
    play_media(mp4_player, "movie.mp4")   # Output: Playing MP4 file: movie.mp4
    play_media(mp3_adapter, "song.mp3")   # Output: Playing MP3 file: song.mp3