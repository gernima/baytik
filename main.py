# !pip install pytelegrambotapi
# !pip install gTTS
# pip install selenium

import telebot
from gtts import gTTS
import subjects, talking, home_work, tests_subjects, gdz

subjects_tf = False
audio = False
gdz_tf = False
dz_tf = False
tests_tf = False
token = '1049041175:AAFHw6FXE2-yCv7L4sJmwg50eImuAusJOG0'
bot = telebot.TeleBot(token)
chromedriver_path = '~/chromedriver'

main_keyboard = telebot.types.ReplyKeyboardMarkup()
main_keyboard.row('Привет')
main_keyboard.row("Предметы", "Тесты")
main_keyboard.row("ГДЗ", "ДЗ")
main_keyboard.row("Хочу пообщаться")
main_keyboard.row("Пока")

subjects_keyboard = telebot.types.ReplyKeyboardMarkup(True)
subjects_keyboard.row('Английский', "Математика", "Русский")
subjects_keyboard.row("Назад")

tests_keyboard = telebot.types.ReplyKeyboardMarkup(True)
tests_keyboard.row('Английский -т', "Математика -т", "Русский -т")
tests_keyboard.row("Назад")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я родился и жду указаний, ' + name(message), reply_markup=main_keyboard)


def name(message):
    return message.from_user.first_name


en_tf = False
en_keyboard = telebot.types.ReplyKeyboardMarkup(True)
en_keyboard.row('Переведи', "Озвучь")
en_keyboard.row("Назад")


def click_subjects_keyboard(message):
    global en_tf, subjects_tf
    if message.text.lower() == 'английский':
        bot.send_message(message.chat.id, "Хорошо пусть будет " + message.text.lower(), reply_markup=en_keyboard)
        en_tf = True
    elif en_tf:
        en_subject(message)
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=main_keyboard)
        subjects_tf = False
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=subjects_keyboard)


def en_subject(message):
    global en_tf
    if message.text.lower() == 'назад':
        en_tf = False
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=subjects_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=en_keyboard)


@bot.message_handler(content_types=['text'])
def send_message(message):
    global audio, gdz_tf, dz_tf, tests_tf, subjects_tf
    if tests_tf:
        tests_tf = False
        # tests parse function
        bot.send_message(message.chat.id, "вывод тестов", reply_markup=main_keyboard)
    elif dz_tf:
        dz_tf = False
        if ' ' in message.text:
            login, password = message.text.split(' ')
            bot.register_next_step_handler(login, password, message, bot, main_keyboard, home_work.click_hm)
        else:
            bot.send_message(message.chat.id, 'Ошибка')
    elif gdz_tf:
        gdz_tf = False

        bot.send_message(message.chat.id, "вывод гдз сайтов", reply_markup=main_keyboard)
    elif subjects_tf:
        click_subjects_keyboard(message)

    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет " + name(message) + ".", reply_markup=main_keyboard)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=main_keyboard)
    elif message.text.lower() == 'гдз':
        gdz_tf = True
        bot.send_message(message.chat.id, 'Введите <название предмета> <класс> <автора>', reply_markup=main_keyboard)
    elif message.text.lower() == 'дз':
        dz_tf = True
        bot.send_message(message.chat.id, 'Введите <логин> <пароль> от edu.tatar', reply_markup=main_keyboard)
    elif message.text.lower() == "предметы":
        subjects_tf = True
        bot.send_message(message.chat.id, 'Вот список предметов', reply_markup=subjects_keyboard)

    elif message.text.lower() == "тесты":
        tests_tf = True
        test_keyboard = tests_subjects.click_tests(message)
        bot.send_message(message.chat.id, 'Введите <название предмета> <класс>', reply_markup=test_keyboard)
    elif message.text.lower() == "хочу пообщаться":
        bot.send_message(message.chat.id, talking.click_talk(message), reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=main_keyboard)


bot.polling()
