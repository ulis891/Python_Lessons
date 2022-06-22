from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from random import randint

TOKEN = '****************************************'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

MAIN = 0
START = 1
MOVE = 2
BOT_MOVE = 3
CANCEL = 4
ERROR = 5

player = ''
candies = 200


def start(update, context):
    global candies
    candies = 200
    context.bot.send_message(update.effective_chat.id,
                             f'На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.'
                             f' Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
                             f' Все конфеты оппонента достаются сделавшему последний ход.\nДля начала игры нажмите /game')




def start_game(update, context):  # Определяем первого игрока
    global player
    start = randint(1, 11)
    if start % 2 == 0:
        player = update.effective_user.first_name
    else:
        player = 'Bot'
    context.bot.send_message(update.effective_chat.id, f'Начинает {player}')
    return START


def error(update, context):
    context.bot.send_message(
        update.effective_chat.id, f'Неверное количество конфет!\nВозьмите от 1 до 28 конфет.\nИли вы ввели не число')
    return MOVE

def bot_move(cand):
    if cand % 29 == 0:
        mv = randint(1, 28)
    else:
        mv = cand - (cand // 29) * 29
    return mv


def player_move(update, context):  # Ход игрока - человека
    # context.bot.send_message(update.effective_chat.id, f'{player}, берите конфеты: ')
    while True:
        try:
            mv = int(update.message.text)
            if 1 <= mv <= 28:
                return mv
            else:
                context.bot.send_message(
                    update.effective_chat.id,
                    f'Неверное количество конфет!\nВозьмите от 1 до 28 конфет.\nИли вы ввели не число')
                return MOVE

        except (ValueError, TypeError):
            return MOVE


def candies_game(update, context):  # Тело игры
    global player, candies
    man = update.effective_user.first_name
    game_bot = 'Bot'
    if candies > 28:
        if player != 'Bot':
            move = player_move(update, context)
            if player == man:
                player = game_bot
            else:
                player = man
            candies -= move
            context.bot.send_message(update.effective_chat.id, f'Осталось конфет: {candies}')
        else:
            move = bot_move(candies)
            candies -= move
            context.bot.send_message(update.effective_chat.id, f'{player} берёт {move} конфет')
            player = man
            context.bot.send_message(update.effective_chat.id, f'Осталось конфет: {candies}')
            context.bot.send_message(update.effective_chat.id, f'{player}, берите конфеты: ')
    else:
        context.bot.send_message(update.effective_chat.id, f'{player}, победил!!!!\nДля новой игры нажмите /start')
        return ConversationHandler.END


def cancel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
game_handler = CommandHandler('game', start_game)
player_handler = MessageHandler(Filters.text, player_move)
start_game_handler = MessageHandler(Filters.text, candies_game)
error_handler = MessageHandler(Filters.text, error)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={START: [start_game_handler],
                                           MOVE: [player_handler],
                                           ERROR: [error_handler]},
                                   fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(game_handler)
dispatcher.add_handler(start_game_handler)

updater.start_polling()
updater.idle()
