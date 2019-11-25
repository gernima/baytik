import telebot
from gtts import gTTS
import enchant
import wikipedia
import re
import sqlite3
from yandex_translate import YandexTranslate
import os, dotenv

dotenv.load_dotenv()
token_yan = os.environ['token_yan']


def create_audio(lang, message):
    tts = gTTS(message.text, lang)
    tts.save('says.mp3')
    file = open('says.mp3', 'rb')
    return file


en_alph = 'abcdefghijklmnopqrstuvwxyz'
ru_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
translate = YandexTranslate(token_yan)


def translating(text):
    try:
        if text.strip()[0] in en_alph:
            a = 'en-ru'
        else:
            a = 'ru-en'
        words = text.split(' ')
        res_word = ''
        for word in words:
            res_word += translate.translate(word, a)['text'][0]
            res_word += ' '
        return res_word
    except:
        return 'Ошибка проверьте предыдущее сообщение'


def check_orphographic(text, lang="ru_RU"):
    try:
        d = enchant.Dict(lang)  # создание словаря для US English (англ язык)
        words = text.split(' ')
        if d.check(text) or (' ' in text and len([x for x in text.split(' ') if not d.check(x)]) == 0):
            return 'Все правильно'  # проверка орфографии (верно)
        res = []
        for word in words:
            if d.check(word):
                res.append(word)
            else:
                res.append(word.upper())
        return ' '.join(res)
    except:
        pass
    return 'Ошибка, проверьте предыдущее сообщение'


def lit_bio_search(what, small=False):
    try:
        some = wikipedia.set_lang("ru")
        some = wikipedia.page(what)
        res = []
        if small:
            search = wikipedia.summary(sentences=10, title=what)  # sentenses - кол-во предложений
            res.append(search)
        else:
            res.append(some.content)
        res.append("\nИсточник: " + some.url)
        return ' '.join(res)
    except:
        return 'Ошибка'


def get_composition(message, bot, keyboard):
    try:
        s = message.text
        con = sqlite3.connect('compositions.db')
        cur = con.cursor()
        s = s.lower()
        s.replace('Сочинение', '')
        s = re.sub(r'\s', '', s)
        s = re.sub(r'[^\w\s]', '', s)
        s = '%' + s + '%'
        res = cur.execute("SELECT content FROM compositions WHERE Name LIKE '{}'".format('%' + s + '%')).fetchone()[0]
        con.close()
        if len(res) != 0:
            a = res.split('\n')
            a = [x for x in a if len(x) != 0]
            q = '\n'.join(a)
            if len(q) > 4000:
                bot.send_message(message.chat.id, q[:4000], reply_markup=keyboard)
                bot.send_message(message.chat.id, q[4000:8000], reply_markup=keyboard)
                try:
                    bot.send_message(message.chat.id, q[8000:12000], reply_markup=keyboard)
                except:
                    pass
                try:
                    bot.send_message(message.chat.id, q[12000:16000], reply_markup=keyboard)
                except:
                    pass
            else:
                bot.send_message(message.chat.id, q, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, 'Сочинение не найдено', reply_markup=keyboard)


def convert_base(num, to_base=10, from_base=16):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

