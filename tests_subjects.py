import telebot


def click_tests(message):
    tests_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    tests_keyboard.row('Английский -т', "Математика -т", "Русский -т")
    tests_keyboard.row("Назад")

    return tests_keyboard
