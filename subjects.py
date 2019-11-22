import telebot
from gtts import gTTS
import enchant
import wikipedia


def create_audio(lang, message):
    tts = gTTS(message.text, lang)
    tts.save('says.mp3')
    file = open('says.mp3', 'rb')
    return file


def translating(text, translate):
    if ' ' in text:
        x = text.split(' ')
        a = x[0]
        words = x[1:]
        res_word = ''
        for word in words:
            res_word += translate.translate(word, a)['text'][0]
            res_word += ' '
        return res_word
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
    return 'Ошибка проверьте предыдущее сообщение'


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

