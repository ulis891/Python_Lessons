import bot_commands as bc
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes




app = ApplicationBuilder().token("*****************************************").build()

app.add_handler(CommandHandler("hello", bc.hello))
app.add_handler(CommandHandler("time", bc.time))
app.add_handler(CommandHandler("help", bc.help))
app.add_handler(CommandHandler("sum", bc.sum))

app.run_polling()
















from isOdd import isOdd

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
#
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()


# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()


