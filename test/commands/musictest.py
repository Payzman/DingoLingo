import discord.ext
import musicbot.commands.music

from unittest import IsolatedAsyncioTestCase


class Test(IsolatedAsyncioTestCase):
    async def test_unknown_youtube_file(self):
        music = musicbot.commands.music.Music(None)
        data = {
            'id': '993251638783520838',
            'attachments': [],
            'embeds': [],
            'edited_timestamp': None,
            'type': discord.MessageType.default,
            'pinned': False,
            'mention_everyone': False,
            'tts': False,
            'content': ''
        }
        msg = discord.Message(state=None, channel=None, data=data)
        ctx = discord.ext.commands.context.Context(message=msg, prefix=None)
        await music._play_song(music, ctx, track="https://open.spotify.com/album"
                                                 "/1VNWqVr6mUMg177IODYb0T?si=XkXdpLrrTKmLitC0gS868g")
