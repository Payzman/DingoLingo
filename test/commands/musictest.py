import musicbot.commands.music as music

from unittest import IsolatedAsyncioTestCase


class Test(IsolatedAsyncioTestCase):
    async def test_unknown_youtube_file(self):
        music_instance = music.Music(None)
        await music_instance._play_song(music_instance, None, track="https://open.spotify.com/album/1VNWqVr6mUMg177IODYb0T?si"
                                                          "=XkXdpLrrTKmLitC0gS868g")
