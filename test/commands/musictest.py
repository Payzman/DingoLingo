import musicbot.commands.music as music


def test_unknown_youtube_file():
    music_instance = music.Music(None)
    music_instance._play_song(None, None,
                              "https://open.spotify.com/album/1VNWqVr6mUMg177IODYb0T?si=XkXdpLrrTKmLitC0gS868g")
