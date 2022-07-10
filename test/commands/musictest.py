import discord.state
import discord.ext
import musicbot.audiocontroller
import musicbot.commands.music
import musicbot.utils

from unittest import IsolatedAsyncioTestCase


class Test(IsolatedAsyncioTestCase):
    async def test_unknown_youtube_file(self):
        music = musicbot.commands.music.Music(None)
        cns = self._setup_connection_state()
        gld = self._setup_guild(cns)
        ctx = self._setup_message_context(cns, gld)
        self._setup_audiocontroller(gld)
        await music._play_song(music, ctx, track="https://open.spotify.com/album"
                                                 "/1VNWqVr6mUMg177IODYb0T?si=XkXdpLrrTKmLitC0gS868g")


    @staticmethod
    def _setup_audiocontroller(guild: discord.Guild):
        musicbot.utils.guild_to_audiocontroller[guild] = musicbot.audiocontroller.AudioController(None, guild)

    @staticmethod
    def _setup_connection_state():
        return discord.state.ConnectionState(
            dispatch=None,
            handlers=None,
            hooks=None,
            syncer=None,
            http=None,
            loop=None
        )

    @staticmethod
    def _setup_guild(state: discord.state.ConnectionState):
        gld_data = {
            'id': '0'
        }
        return discord.Guild(data=gld_data, state=state)

    @staticmethod
    def _setup_message_context(state: discord.state.ConnectionState, guild: discord.guild.Guild):
        chn_data = {
            'id': '0',
            'type': discord.ChannelType.text,
            'name': 'my-text-channel',
            'position': 0,
        }
        chn = discord.TextChannel(state=state, guild=guild, data=chn_data)
        msg_data = {
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
        msg = discord.Message(state=state, channel=chn, data=msg_data)
        ctx = discord.ext.commands.context.Context(message=msg, prefix=None)
        return ctx
