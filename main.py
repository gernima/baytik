# !pip install pytelegrambotapi
# !pip install gTTS

import telebot
from gtts import gTTS
import subjects, talking, home_work, tests_subjects, gdz

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


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я родился и жду указаний, ' + name(message), reply_markup=main_keyboard)


def name(message):
    return message.from_user.first_name

def en_subjects_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Переведи", "Озвучь")

    return keyboard


@bot.message_handler(content_types=['text'])
def send_message(message):
    global audio
    global gdz_tf
    global dz_tf
    global tests_tf
    if tests_tf:
        tests_tf = False
        # tests parse function
        bot.send_message(message.chat.id, "вывод тестов", reply_markup=main_keyboard)
    elif dz_tf:
        dz_tf = False
        login, password = message.split(' ')
        bot.register_next_step_handler(message, home_work.click_hm(login, password, message, bot, main_keyboard))
    elif gdz_tf:
        gdz_tf = False

        bot.register_next_step_handler(message, gdz.click_gdz(message, bot, main_keyboard))
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
        subjects_keyboard = subjects.click_subjects(message)
        bot.send_message(message.chat.id, 'Вот список предметов', reply_markup=subjects_keyboard)
    elif message.text.lower() == "тесты":
        test_keyboard = tests_subjects.click_tests(message)
        bot.send_message(message.chat.id, 'Введите <название предмета> <класс>', reply_markup=test_keyboard)
    elif message.text.lower() == "хочу пообщаться":
        bot.send_message(message.chat.id, talking.click_talk(message), reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю", reply_markup=main_keyboard)


bot.polling(none_stop=True)
