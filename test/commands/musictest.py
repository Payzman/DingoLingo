import discord.ext
import musicbot.commands.music

from unittest import IsolatedAsyncioTestCase


class Test(IsolatedAsyncioTestCase):
    async def test_unknown_youtube_file(self):
        music = musicbot.commands.music.Music(None)
        data = {
            'id': '0',
            'attachments': [],
            'embeds': [],
            'edited_timestamp': None,
            'type': discord.MessageType.default,
            'pinned': False,
            'mention_everyone': False,
            'tts': False,
            'content': ''
        }
        gld = discord.Guild(data=None, state=None)
        chn = discord.TextChannel(state=None, guild=gld, data=None)
        msg = discord.Message(state=None, channel=chn, data=data)
        ctx = discord.ext.commands.context.Context(message=msg, prefix=None)
        await music._play_song(music, ctx, track="https://open.spotify.com/album"
                                                 "/1VNWqVr6mUMg177IODYb0T?si=XkXdpLrrTKmLitC0gS868g")
