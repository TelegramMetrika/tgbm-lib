import aiogram
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

######## EXAMPLE ########
from aiogram import middlewares
from tgbm_lib import Logger, ServerSender
sender = ServerSender(
    token='metrika_token_here',    # <---
    server='metrika_url_here'      # <---
)
logger = Logger(sender)

class StatMiddleware(middlewares.BaseMiddleware):
    def __init__(self):
        super(StatMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        await logger.write_logs(self._manager.bot.id, message, parse_text=True)

dp.middleware.setup(StatMiddleware())
######## END ########

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('+')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 