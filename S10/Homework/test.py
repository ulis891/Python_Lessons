from telegram import Update, Bot, update
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from random import randint, choice

TOKEN = '5325614124:AAFagHdyETOnLB6C8_m4J6NdKQNfPMrpiYM'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

player = ''
user = update.effective_user.first_name


def start(update, context):
    global candies
    candies = 200
    context.bot.send_message(update.effective_chat.id,
                             f'На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.'
                             f' Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
                             f' Все конфеты оппонента достаются сделавшему последний ход.\nДля начала игры нажмите /game')


def choice_first_player():
    player = choice('bot', user)
    return player


def bot_move(cand, update, context):
    if cand % 29 == 0:
        mv = randint(1, 28)
    else:
        mv = cand - (cand // 29) * 29
    context.bot.send_message(update.effective_chat.id, f'Bot берёт {mv} конфет')
    return mv

def player_move(update, context):
    move = mv = int(update.message.text)

    pass
