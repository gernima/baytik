import telebot


def click_subjects(message):
    subjects_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    subjects_keyboard.row('Английский', "Математика", "Русский")
    subjects_keyboard.row("Назад")

    return subjects_keyboard
