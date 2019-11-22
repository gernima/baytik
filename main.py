# !pip install pytelegrambotapi
# !pip install gTTS
# pip install selenium
# pip install yandex_translate

import telebot
from gtts import gTTS
import subjects, talking, home_work, tests_subjects, gdz
from yandex_translate import YandexTranslate

token = '1049041175:AAFHw6FXE2-yCv7L4sJmwg50eImuAusJOG0'
bot = telebot.TeleBot(token)
chromedriver_path = '~/chromedriver'
translate = YandexTranslate('trnsl.1.1.20191118T112631Z.f64a9d42a3ccc05f.2d0224570891cba3621e2cb1266bcd89f471813f')

main_keyboard = telebot.types.ReplyKeyboardMarkup()
main_keyboard.row('Привет')
main_keyboard.row("Предметы", "Тесты")
main_keyboard.row("ГДЗ", "ДЗ")
main_keyboard.row("Хочу пообщаться")

subjects_keyboard = telebot.types.ReplyKeyboardMarkup(True)
subjects_keyboard.row('Английский', "Математика", "Русский")
subjects_keyboard.row("Информатика", 'Литература')
subjects_keyboard.row("Назад")

tests_keyboard = telebot.types.ReplyKeyboardMarkup(True)
tests_keyboard.row('Английский -т', "Математика -т", "Русский -т")
tests_keyboard.row("Назад")

en_keyboard = telebot.types.ReplyKeyboardMarkup(True)
en_keyboard.row('Переведи', "Озвучь")
en_keyboard.row("Назад")

ru_keyboard = telebot.types.ReplyKeyboardMarkup(True)
ru_keyboard.row('Переведи', "Озвучь")
ru_keyboard.row("Проверь на орфографию")
ru_keyboard.row("Назад")

lit_keyboard = telebot.types.ReplyKeyboardMarkup(True)
lit_keyboard.row('Найди сочинение')
lit_keyboard.row("биография (кратко)")
lit_keyboard.row("биография (полная)")
lit_keyboard.row("Назад")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я родился и жду указаний, ' + name(message), reply_markup=main_keyboard)


def name(message):
    return message.from_user.first_name


def click_subjects_keyboard(message):
    if message.text.lower() == 'английский':
        bot.send_message(message.chat.id, "Хорошо, пусть будет " + message.text.lower(), reply_markup=en_keyboard)
        bot.register_next_step_handler(message, en_subject)
    elif message.text.lower() == 'русский':
        bot.send_message(message.chat.id, "Хорошо, пусть будет " + message.text.lower(), reply_markup=ru_keyboard)
        bot.register_next_step_handler(message, ru_subject)
    elif message.text.lower() == 'литература':
        bot.send_message(message.chat.id, "Хорошо, пусть будет " + message.text.lower(), reply_markup=lit_keyboard)
        bot.register_next_step_handler(message, lit_subject)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=main_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)


def translate_word(message, keyboard, func):
    bot.send_message(message.chat.id, subjects.translating(message.text, translate), reply_markup=keyboard)
    bot.register_next_step_handler(message, func)


def en_subject(message, keyboard=en_keyboard):
    if message.text.lower() == 'озвучь':
        bot.send_message(message.chat.id, 'Введите текст и подождите')
        bot.register_next_step_handler(message, audio, keyboard, 'en', en_subject)
    elif message.text.lower() == 'переведи':
        bot.send_message(message.chat.id,
                         'Введите с какого языка на какой и текст \n(Например, ru-en привет, en-ru hello)')
        bot.register_next_step_handler(message, translate_word, en_keyboard, en_subject)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=en_keyboard)
        bot.register_next_step_handler(message, en_subject)


def audio(message, keyboard, lang, func):
    bot.send_audio(message.chat.id, subjects.create_audio(lang, message), reply_markup=keyboard)
    bot.register_next_step_handler(message, func)


def orf(message, keyboard, lang, func):
    bot.send_message(message.chat.id, subjects.check_orphographic(message.text, lang), reply_markup=keyboard)
    bot.register_next_step_handler(message, func)


def ru_subject(message, keyboard=ru_keyboard):
    if message.text.lower() == 'озвучь':
        bot.send_message(message.chat.id, 'Введите текст и подождите')
        bot.register_next_step_handler(message, audio, keyboard, 'ru', ru_subject)
    elif message.text.lower() == 'проверь на орфографию':
        bot.send_message(message.chat.id, 'Введите текст и подождите')
        bot.register_next_step_handler(message, orf, ru_keyboard, 'ru_RU', ru_subject)
    elif message.text.lower() == 'переведи':
        bot.send_message(message.chat.id,
                         'Введите с какого языка на какой и текст \n(Например, ru-en привет, en-ru hello)')
        bot.register_next_step_handler(message, translate_word, ru_keyboard, ru_subject)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=keyboard)
        bot.register_next_step_handler(message, ru_subject)


def lit_bio_small(message):
    bot.send_message(message.chat.id, subjects.lit_bio_search(message.text, True), reply_markup=lit_keyboard)
    bot.register_next_step_handler(message, lit_subject)


def lit_bio_long(message):
    bot.send_message(message.chat.id, subjects.lit_bio_search(message.text), reply_markup=lit_keyboard)
    bot.register_next_step_handler(message, lit_subject)


def lit_work(message):
    bot.register_next_step_handler(message, lit_subject)


def lit_subject(message, keyboard=lit_keyboard):
    if message.text.lower() == 'найди сочинение':
        bot.send_message(message.chat.id, 'Введите название сочинения', reply_markup=keyboard)
        bot.register_next_step_handler(message, lit_work)
    elif message.text.lower() == 'биография (полная)':
        bot.send_message(message.chat.id, 'Введите ваш запрос', reply_markup=keyboard)
        bot.register_next_step_handler(message, lit_bio_long)
    elif message.text.lower() == 'биография (кратко)':
        bot.send_message(message.chat.id, 'Введите ваш запрос', reply_markup=keyboard)
        bot.register_next_step_handler(message, lit_bio_small)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=keyboard)
        bot.register_next_step_handler(message, lit_subject)


def get_dz(message):
    if ' ' in message.text:
        login, password = message.text.split(' ')
        home_work.click_hm(login, password, message, bot, main_keyboard)
    else:
        bot.send_message(message.chat.id, 'Проверьте логин и пароль')


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет " + name(message) + ".", reply_markup=main_keyboard)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=main_keyboard)
    elif message.text.lower() == 'гдз':
        bot.send_message(message.chat.id, 'Введите <название предмета> <класс> <автора>', reply_markup=main_keyboard)
    elif message.text.lower() == 'дз':
        bot.send_message(message.chat.id, 'Введите <логин> <пароль> от edu.tatar', reply_markup=main_keyboard)
        bot.register_next_step_handler(message, get_dz)
    elif message.text.lower() == "предметы":
        bot.send_message(message.chat.id, 'Вот список предметов', reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    elif message.text.lower() == "тесты":
        test_keyboard = tests_subjects.click_tests(message)
        bot.send_message(message.chat.id, 'Введите <название предмета> <класс>', reply_markup=test_keyboard)
    elif message.text.lower() == "хочу пообщаться":
        bot.send_message(message.chat.id, talking.click_talk(message), reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=main_keyboard)


bot.polling()
