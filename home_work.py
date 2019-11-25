from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs


def click_hm(login, password, message, bot, keyboard):
    try:
        # login, password = message.text.split(' ')
        print(login, password)
        dz = parsing(login, password)
        s = ''
        dz = [x for x in dz if x]
        for i in dz:
            for j in i:
                s += j.replace('\t', '').replace('\r', '')
            s += '\n'
        bot.send_message(message.chat.id, s, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, "Неверный логин пароль или edu.tatar не доступен в вашей стране")


def login_with_requests(session, login, password):
    payload = {'main_login': login, 'main_password': password}
    url = 'https://edu.tatar.ru/logon'
    headers = {'Referer': url}
    responce = session.post(url,
                            data=payload,
                            headers=headers)


def parsing(login, password):  # local - 33 sec
    day_url = 'https://edu.tatar.ru/user/diary/day'
    s = requests.Session()
    login_with_requests(s, login, password)
    res = s.get(day_url)
    html = res.text
    soup = bs(html)
    table = soup.find('tbody')
    day_subjects = table.find_all('tr')
    day_subjects = [subject.text.split('\n') for subject in day_subjects]
    for i in range(len(day_subjects)):
        day_subjects[i] = [line for line in day_subjects[i] if line != '']
    return day_subjects


