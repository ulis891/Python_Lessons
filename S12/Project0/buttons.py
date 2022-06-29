from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler

TOKEN = '5325614124:AAFagHdyETOnLB6C8_m4J6NdKQNfPMrpiYM'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    keyboard = [[InlineKeyboardButton('1', callback_data='1'), InlineKeyboardButton('2', callback_data='2')],
                [InlineKeyboardButton('3', callback_data='3'), InlineKeyboardButton('4', callback_data='4')]]
    update.message.reply_text('Вбери цифру: ', reply_markup=InlineKeyboardMarkup(keyboard))


def button(update, context):
    query = update.callback_query
    print(query.data)
    context.bot.send_message(update.effective_chat.id, f'Вы нажали на {query.data} кнопку')


def poll(update, context):
    question = 'Как твои дела?'
    answer = ['Отлично', 'Хорошо', 'Не очень', 'Меня бесит жара']

    message = context.bot.send_poll(update.effective_chat.id, question, answer,
                                    is_anonymous=False, allows_multiple_answers=False)
    payload = {
        message.poll.id: {
            'questions': question,
            'massage_id': message.message_id,
            'chat_id': update.effective_chat.id,
            'answers': 0
        }
    }
    context.bot_data.update(payload)


poll_handler = CommandHandler('poll', poll)
button_handler = CallbackQueryHandler(button)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(poll_handler)

updater.start_polling()
updater.idle()
