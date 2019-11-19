import telebot


def click_gdz(message, bot, keyboard):

    bot.send_message(message.chat.id, "вывод гдз сайтов", reply_markup=keyboard)
