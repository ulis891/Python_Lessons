"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5325614124:AAFagHdyETOnLB6C8_m4J6NdKQNfPMrpiYM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

@dp.message_handler()
async def typel(message: types.Sticker):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer('Nahuy poshol')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)