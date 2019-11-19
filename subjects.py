import telebot

en_tf = False
en_keyboard = telebot.types.ReplyKeyboardMarkup(True)
en_keyboard.row('Переведи', "Озвучь")
en_keyboard.row("Назад")


def click_subjects_keyboard(message, bot, keyboard):
    global en_tf
    print(1)
    if message.text.lower() == 'английский':
        bot.send_message(message.chat.id, "Хорошо пусть будет " + message.text.lower(), reply_markup=en_keyboard)
        bot.register_next_step_handler(message, bot, keyboard, en_subject)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=keyboard)


def en_subject(message, bot, keyboard):
    global en_tf
    print(2)
    if message.text.lower() == 'назад':
        en_tf = False
        print(1)
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=keyboard)
