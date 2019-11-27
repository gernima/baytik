# !pip install pytelegrambotapi
# !pip install gTTS
# pip install selenium
# pip install yandex_translate
# pip install apiai

# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from gtts import gTTS
import subjects, home_work, tests_subjects, gdz
import apiai, json
import os, dotenv

dotenv.load_dotenv()
token = os.environ['token']
token_ii = os.environ['token_ii']
bot = telebot.TeleBot(token)
# chromedriver_path = '~/chromedriver'

main_keyboard = telebot.types.ReplyKeyboardMarkup()
main_keyboard.row('Привет')
main_keyboard.row("Предметы", "Тесты")
main_keyboard.row("ДЗ")
main_keyboard.row("Хочу пообщаться")

subjects_keyboard = telebot.types.ReplyKeyboardMarkup(True)
subjects_keyboard.row('Английский', "Русский")
subjects_keyboard.row("Информатика", 'Литература')
subjects_keyboard.row("Физика", "История")
subjects_keyboard.row("Назад")

tests_keyboard = telebot.types.ReplyKeyboardMarkup(True)
tests_keyboard.row("ОГЭ", "ЕГЭ")
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
lit_keyboard.row("биография (кратко)", "биография (полная)")
lit_keyboard.row('Шпаргалка')
lit_keyboard.row("Назад")

talk_keyboard = telebot.types.ReplyKeyboardMarkup(True)
talk_keyboard.row('назад')

inf_keyboard = telebot.types.ReplyKeyboardMarkup(True)
inf_keyboard.row("Перевод СС")
# inf_keyboard.row("python cheat sheet list")
inf_keyboard.row("законы логики", "Степень двойки")
inf_keyboard.row("Назад")

fiz_keyboard = telebot.types.ReplyKeyboardMarkup(True)
fiz_keyboard.row("Механика", "Молекулярная физика. Термодинамика")
fiz_keyboard.row("Электродинамика. Электростатика", "Оптика")
fiz_keyboard.row("Назад")

his_keyboard = telebot.types.ReplyKeyboardMarkup(True)
his_keyboard.row("Найди дату")
his_keyboard.row("Назад")

dz_keyboard = telebot.types.ReplyKeyboardMarkup(True)
dz_keyboard.row("Дз на сегодня", "Дз на завтра")
dz_keyboard.row("Авторизация")
dz_keyboard.row("Назад")


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
    elif message.text.lower() == "информатика":
        bot.send_message(message.chat.id, "Хорошо, пусть будет " + message.text.lower(), reply_markup=inf_keyboard)
        bot.register_next_step_handler(message, inf_subject)
    elif message.text.lower() == "физика":
        bot.send_message(message.chat.id, "Хорошо, пусть будет " + message.text.lower(), reply_markup=fiz_keyboard)
        bot.register_next_step_handler(message, fiz_subject)
    elif message.text.lower() == "история":
        bot.send_message(message.chat.id, "Хорошо, пусть будет " + message.text.lower(), reply_markup=his_keyboard)
        bot.register_next_step_handler(message, his_subject)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=main_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)


def his_get_date(message):
    bot.send_message(message.chat.id, subjects.get_date(message.text.lower()), reply_markup=his_keyboard)
    bot.register_next_step_handler(message, his_subject)


def his_subject(message, keyboard=his_keyboard):
    if message.text.lower() == "найди дату":
        bot.send_message(message.chat.id, "Введите дату", reply_markup=keyboard)
        bot.register_next_step_handler(message, his_get_date)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=keyboard)
        bot.register_next_step_handler(message, his_subject)


def fiz_subject(message, keyboard=fiz_keyboard):
    if message.text.lower() == "механика":
        bot.send_photo(message.chat.id, open('cribs/fiz/mechanica.jpg', 'rb'), reply_markup=keyboard)
        bot.register_next_step_handler(message, fiz_subject)
    elif message.text.lower() == "молекулярная физика. термодинамика":
        bot.send_photo(message.chat.id, open('cribs/fiz/molekyl.png', 'rb'), reply_markup=keyboard)
        bot.send_photo(message.chat.id, open('cribs/fiz/teplovye.png', 'rb'), reply_markup=keyboard)
        bot.register_next_step_handler(message, fiz_subject)
    elif message.text.lower() == "электродинамика. электростатика":
        bot.send_photo(message.chat.id, open('cribs/fiz/elektro.jpeg', 'rb'), reply_markup=keyboard)
        bot.register_next_step_handler(message, fiz_subject)
    elif message.text.lower() == "оптика":
        bot.send_photo(message.chat.id, open('cribs/fiz/optika.png', 'rb'), reply_markup=keyboard)
        bot.register_next_step_handler(message, fiz_subject)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=keyboard)
        bot.register_next_step_handler(message, fiz_subject)


def translate_word(message, keyboard, func):
    bot.send_message(message.chat.id, subjects.translating(message.text), reply_markup=keyboard)
    bot.register_next_step_handler(message, func)


def en_subject(message, keyboard=en_keyboard):
    if message.text.lower() == 'озвучь':
        bot.send_message(message.chat.id, 'Введите текст и подождите')
        bot.register_next_step_handler(message, audio, keyboard, 'en', en_subject)
    elif message.text.lower() == 'переведи':
        bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(message, translate_word, en_keyboard, en_subject)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=en_keyboard)
        bot.register_next_step_handler(message, en_subject)


def audio(message, keyboard, lang, func):
    bot.send_audio(message.chat.id, subjects.create_audio(message), reply_markup=keyboard)
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
        bot.send_message(message.chat.id, 'Введите текст')
        bot.register_next_step_handler(message, translate_word, ru_keyboard, ru_subject)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=keyboard)
        bot.register_next_step_handler(message, ru_subject)


def lit_bio_small(message):
    bot.send_message(message.chat.id, subjects.lit_bio_search(message.text, True), reply_markup=lit_keyboard)
    bot.register_next_step_handler(message, lit_subject)


def lit_bio_long(message):
    bot.send_message(message.chat.id, subjects.lit_bio_search(message.text), reply_markup=lit_keyboard)
    bot.register_next_step_handler(message, lit_subject)


def lit_work(message):
    subjects.get_composition(message, bot, lit_keyboard)
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
    elif message.text.lower() == "шпаргалка":
        try:
            bot.send_message(message.chat.id, 'https://drive.google.com/open?id=1_3h8_9qVg_52fpu43tYM--uvYV3qcqYU',
                             reply_markup=keyboard)
        except:
            bot.send_message(message.chat.id, 'Ошибка', reply_markup=keyboard)
        bot.register_next_step_handler(message, lit_subject)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=keyboard)
        bot.register_next_step_handler(message, lit_subject)


def inf_get(message):
    try:
        num, from_, to = map(int, message.text.split())
        bot.send_message(message.chat.id, subjects.convert_base(str(num), from_base=from_, to_base=to),
                         reply_markup=inf_keyboard)
    except:
        bot.send_message(message.chat.id, 'Сообщение нужно вводить в правильном формате\n'
                         '<Число> <текущая система счисления> <в какую нужно перевести>')
    bot.register_next_step_handler(message, inf_subject)


def inf_subject(message, keyboard=inf_keyboard):
    if message.text.lower() == "перевод сс":
        bot.send_message(message.chat.id,
                         "Введите через пробел число, с какой в какую систему счисления\n Пример: 100101 10 2",
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, inf_get)
    elif message.text.lower() == 'законы логики':
        bot.send_photo(message.chat.id, open("cribs/inf/Zakony logiki.jpg", 'rb'), reply_markup=keyboard)
        bot.register_next_step_handler(message, inf_subject)
    elif message.text.lower() == 'перевод данных':
        bot.send_photo(message.chat.id, open("cribs/inf/перевод данных.jpg", 'rb'), reply_markup=keyboard)
        bot.register_next_step_handler(message, inf_subject)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=keyboard)
        bot.register_next_step_handler(message, inf_subject)


def get_dz(message, this_day):
    try:
        if this_day:
            home_work.click_hm(True, message, bot, dz_keyboard)
        else:
            home_work.click_hm(False, message, bot, dz_keyboard)
    except:
        bot.send_message(message.chat.id, 'Проверьте логин и пароль указаный при авторизации, и заново авторизуйтесь',
                         reply_markup=dz_keyboard)
    bot.register_next_step_handler(message, dz)


def reg_user(message, keyboard):
    home_work.write_login_password(message, bot, keyboard)
    bot.register_next_step_handler(message, dz)


# def new_dz(message, day):
#     try:
#         if ' ' in message.text:
#             login, password = message.text.split(' ')
#             if day:
#                 home_work.click_hm(True, message, bot, dz_keyboard, login, password)
#             else:
#                 home_work.click_hm(False, message, bot, dz_keyboard, login, password)
#         else:
#             bot.send_message(message.chat.id, 'Логин и пароль нужно писать через пробел', reply_markup=dz_keyboard)
#     except:
#         bot.send_message(message.chat.id, 'Проблемы с прокси, попробуйте повторить', reply_markup=dz_keyboard)
#     bot.register_next_step_handler(message, dz)


def dz(message, keyboard=dz_keyboard):
    if message.text.lower() == 'дз на сегодня':
        get_dz(message, True)
        # bot.send_message(message.chat.id, "Введите логин и пароль через пробел\nПример: 123456789 123456789",
        #                  reply_markup=keyboard)
        # bot.register_next_step_handler(message, new_dz, True)
    elif message.text.lower() == 'дз на завтра':
        get_dz(message, False)
        # bot.send_message(message.chat.id, "Введите логин и пароль через пробел\nПример: 123456789 123456789",
        #                  reply_markup=keyboard)
        # bot.register_next_step_handler(message, new_dz, False)
    elif message.text.lower() == 'авторизация':
        bot.send_message(message.chat.id, 'Введите логин и пароль через пробел.\nПривер: 123456789 123456789',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, reg_user, keyboard)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=main_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=keyboard)
        bot.register_next_step_handler(message, dz)


def click_talk(message):
    request = apiai.ApiAI(token_ii).text_request()  # Токен API к Dialogflow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message.text  # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response != '':
        bot.send_message(message.chat.id, response, reply_markup=talk_keyboard)
        bot.register_next_step_handler(message, click_talk)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Пока', reply_markup=main_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=talk_keyboard)
        bot.register_next_step_handler(message, click_talk)


def get_oge(message):
    bot.send_message(message.chat.id, tests_subjects.oge(message.text))
    bot.register_next_step_handler(message, tests)


def get_ege(message):
    bot.send_message(message.chat.id, tests_subjects.ege(message.text))
    bot.register_next_step_handler(message, tests)


def tests(message):
    if message.text.lower() == 'огэ':
        bot.send_message(message.chat.id, 'Введите <название предмета> <вариант>', reply_markup=tests_keyboard)
        bot.register_next_step_handler(message, get_oge)
    elif message.text.lower() == 'егэ':
        bot.send_message(message.chat.id, 'Введите <название предмета> <вариант>', reply_markup=tests_keyboard)
        bot.register_next_step_handler(message, get_ege)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Хорошо', reply_markup=main_keyboard)
        bot.register_next_step_handler(message, send_message)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=tests_keyboard)
        bot.register_next_step_handler(message, tests)


def send_gdz(message):
    bot.send_message(message.chat.id, gdz.get_gdz(message.text))
    bot.register_next_step_handler(message, send_message)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет " + name(message) + ".", reply_markup=main_keyboard)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=main_keyboard)
    # elif message.text.lower() == 'гдз':
    #     bot.send_message(message.chat.id, 'Введите <название предмета> <класс> <автора> <номер задания>',
    #                      reply_markup=main_keyboard)
    #     bot.register_next_step_handler(message, send_gdz)
    elif message.text.lower() == 'дз':
        bot.send_message(message.chat.id, 'Перед запросом авторизуйтесь, если вы этого не сделали',
                         reply_markup=dz_keyboard)
        bot.register_next_step_handler(message, dz)
    elif message.text.lower() == "предметы":
        bot.send_message(message.chat.id, 'Вот список предметов', reply_markup=subjects_keyboard)
        bot.register_next_step_handler(message, click_subjects_keyboard)
    elif message.text.lower() == "тесты":
        bot.send_message(message.chat.id,
                         'Список предметов: Математика, Информатика, Русский, Английский, Физика, Химия, Биология, '
                         'География, Обществознание, Литература, История\nВыберите вариант от 1 до 15',
                         reply_markup=tests_keyboard)
        bot.register_next_step_handler(message, tests)
    elif message.text.lower() == "хочу пообщаться":
        bot.send_message(message.chat.id, 'Привет', reply_markup=talk_keyboard)
        bot.register_next_step_handler(message, click_talk)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=main_keyboard)


bot.polling()
