from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, filters


bot = Bot(token='5325614124:AAFagHdyETOnLB6C8_m4J6NdKQNfPMrpiYM')
updater = Updater(bot, update_queue=True)
dispatcher = Updater


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Hello!")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создала компания GB!")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()