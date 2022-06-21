from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler
from datetime import datetime

TOKEN = '**********:***********************************'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f"Hello {update.effective_user.first_name}!\nДавай посчитаем комплексные числа!")
    context.bot.send_message(update.effective_chat.id,
                             f"Введите, что будем делать:\n/sum\t(сложение)\n/dif\t(вычитание)\n"
                             f"/mult\t(умножение)\n/div\t(деление)\n"
                             f"и добавьте через пробел 4 аргумента где:\n"
                             f"1 - истиная часть первого аргумента\n"
                             f"2 - мнимая часть первого аргумента\n"
                             f"3 - истиная часть второго аргумента\n"
                             f"4 - мнимая часть второго аргумента")


def log(x, action, y, result):
    count = 0
    with open('log.txt', 'r', encoding='utf-8') as log:
        for row in log:
            count += 1
    time = datetime.now()
    with open('log.txt', 'a+', encoding='utf-8') as log:
        log.write(f'{count};{time};{x};{action};{y};{result}\n')


def sum(update, context):
    arg = context.args
    a, b, c, d = list(map(int, arg))
    x = complex(a, b)
    y = complex(c, d)
    result = x + y
    context.bot.send_message(update.effective_chat.id, f"{x} + {y} = {result}")
    log(x, '+', y, result)


def dif(update, context):
    arg = context.args
    a, b, c, d = list(map(int, arg))
    x = complex(a, b)
    y = complex(c, d)
    result = x - y
    context.bot.send_message(update.effective_chat.id, f"{x} - {y} = {result}")
    log(x, '-', y, result)


def multi(update, context):
    arg = context.args
    a, b, c, d = list(map(int, arg))
    x = complex(a, b)
    y = complex(c, d)
    result = x * y
    context.bot.send_message(update.effective_chat.id, f"{x} * {y} = {result}")
    log(x, '*', y, result)


def div(update, context):
    arg = context.args
    a, b, c, d = list(map(int, arg))
    x = complex(a, b)
    y = complex(c, d)
    result = x / y
    context.bot.send_message(update.effective_chat.id, f"{x} / {y} = {result}")
    log(x, '/', y, result)


start_handler = CommandHandler('start', start)
sum_handler = CommandHandler("sum", sum)
dif_handler = CommandHandler("dif", dif)
multi_handler = CommandHandler("mult", multi)
div_handler = CommandHandler("div", div)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(dif_handler)
dispatcher.add_handler(multi_handler)
dispatcher.add_handler(div_handler)

updater.start_polling()
updater.idle()
