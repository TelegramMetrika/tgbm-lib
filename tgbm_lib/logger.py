from aiogram import types
from datetime import datetime


class Logger:
    """
    Class parses data from telegram bot
    then send it to storage
    """
    def __init__(self, sender_class=None) -> None:
        self.sender_class = sender_class

    def parse_data(self,  bot_id: int,
                   message: types.Message,
                   parse_text) -> dict:
        # ...
        return message

    async def write_logs(self, bot_id: int,
                         message: types.Message,
                         parse_text=False) -> None:
        """
        Pass data to sender class

        Args:
            bot_id (int): bot id (self._manager.bot.id)
            message (types.Message):
            parse_text (bool, optional): pass text to db. Defaults to False.
        """
        data = self.parse_data(bot_id, message, parse_text)
        await self.sender_class.write_message(data)
