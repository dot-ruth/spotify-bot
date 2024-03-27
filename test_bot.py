import bot
import unittest
from unittest.mock import MagicMock

class TestSpotifyBot(unittest.TestCase):
    def test_start_command(self):
        update = MagicMock()
        context = MagicMock()

        bot.start(update, context)

        context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id, text="""
    Welcome to the Spotify Telegram Bot!

    Here are the available commands:
    /search - Perform a search
    /random - Get a random song
    /browse - Discover music
    """)

    def test_search_command(self):
        update = MagicMock()
        context = MagicMock()
        update.message.text = "test search query"

        bot.process_search_query(update, context)


    def test_random_command(self):
        update = MagicMock()
        context = MagicMock()

        bot.random_track(update, context)


    def test_browse_command(self):
        update = MagicMock()
        context = MagicMock()

        bot.browse(update, context)


if __name__ == '__main__':
    unittest.main()
