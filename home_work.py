import requests
from bs4 import BeautifulSoup as bs


# ! /usr/bin/env python
# -*- coding: utf-8 -*-


def read_login_password(message, bot, keyboard):
    login = ''
    with open('edu.txt', 'r') as file:
        data = file.read()
        a = data.split('\n')
        for i in a:
            x = i.split(':')
            if x[0] == str(message.chat.id):
                login = x[1].split(' ')[0]
                password = x[1].split(' ')[1]
        # if len(login):
        #     bot.send_message(message.chat.id, 'Сперва авторизируйтесь', reply_markup=keyboard)
    return login, password


def write_login_password(message, bot, keyboard):
    if ' ' in message.text:
        with open('edu.txt', 'r+') as f:
            data = f.read().strip().split('\n')
            for i in range(len(data)):
                if data[i].split(':')[0] == str(message.chat.id):
                    data[i] = ''
        data = [x.replace('\n', '') for x in data]
        with open('edu.txt', 'w') as f:
            f.write(
                '\n'.join(data).strip() + '\n' + str(message.chat.id) + ':' + str(
                    message.text.split(' ')[0]) + ' ' + str(
                    message.text.split()[1]))

        bot.send_message(message.chat.id, 'Вы успешно авторизовались', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Логин и пароль нужно писать через пробел', reply_markup=keyboard)


def click_hm(this_day, message, bot, keyboard):
    # try:
    login, password = read_login_password(message, bot, keyboard)
    dz = parsing(login, password, this_day)
    s = ''
    dz = [x for x in dz if x]
    for i in dz:
        for j in i:
            s += j.replace('\t', '').replace('\r', '') + ' | '
        s += '\n'
    bot.send_message(message.chat.id, s, reply_markup=keyboard)
    # print(s)


# except:
#    bot.send_message(message.chat.id, 'Проверьте логин и пароль', reply_markup=keyboard)


def login_with_requests(session, login, password):
    payload = {'main_login': login, 'main_password': password}
    url = 'https://edu.tatar.ru/logon'
    headers = {'Referer': url}
    responce = session.post(url,
                            data=payload,
                            headers=headers)


def parsing(login, password, this_day):  # local - 33 sec
    day_url = 'https://edu.tatar.ru/user/diary/day'
    s = requests.Session()
    s.proxies = {"https": "http://86.62.120.68:3128", "https": "http://176.123.164.78:3128",
                 "https": "http://91.245.36.186:8080",
                 "https": "http://78.110.154.177:59888", "https": "http://79.175.57.77:55477",
                 "https": "http://92.39.221.36:8080",
                 "https": "http://37.98.242.212:8080", "https": "http://81.163.59.162:41258",
                 "https": "http://91.210.198.22:8080",
                 "http": "http://212.188.66.218:8080	", "http": "http://80.234.38.44:3128",
                 "http": "http://109.60.154.31:50594",
                 "https": "http://176.214.224.168:8080", "https": "http://213.138.71.118:81",
                 "http": "http://213.167.215.196:8080",
                 "https": "http://5.165.241.198:8080", "http": "http://176.123.164.78:3128",
                 "http": "http://79.137.254.51:40779",
                 "https": "http://37.208.127.181:8080", "https": "http://79.175.57.77:55477",
                 "http": "http://85.26.146.169:80",
                 "https": "http://194.143.151.96:5011", "http": "http://78.110.154.177:59888",
                 "https": "http://85.113.39.89:81",
                 "http": "http://89.255.83.199:50234", "http": "http://95.31.245.50:36568",
                 "http": "http://37.78.206.136:8080",
                 "https": "http://109.74.132.190:46177", "https": "http://62.173.145.48:3128",
                 "https": "http://82.202.176.40:3128",
                 "https": "http://195.239.178.110:33246", "http": "http://80.234.38.44:3128",
                 "https": "http://194.226.34.132:5555",
                 "https": "http://46.39.245.204:36950", "https": "http://193.111.3.186:3128",
                 "https": "http://37.208.127.181:8080",
                 "https": "http://109.248.62.207:42226", "https": "http://5.1.53.46:8080",
                 "http": "http://77.232.167.200:51288"
                 }
    login_with_requests(s, login, password)
    res = s.get(day_url)
    html = res.text
    soup = bs(html, 'html.parser')
    if not this_day:
        next_day_url = soup.find('span', 'nextd').find('a')['href']
        res = s.get(next_day_url)
        html = res.text
        soup = bs(html, 'html.parser')
    table = soup.find('tbody')
    day_subjects = table.find_all('tr')
    day_subjects = [subject.text.split('\n') for subject in day_subjects]
    for i in range(len(day_subjects)):
        day_subjects[i] = [line for line in day_subjects[i] if line != '']
    return day_subjects
