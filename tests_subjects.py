import requests
import urllib3
import json
from bs4 import BeautifulSoup as bs


def oge(text):
    try:
        subject = text.split(' ')[0]
        var = int(text.split(' ')[1])
        if subject.lower() == 'биология':

            list_ = []

            for i in range(1467058, 1467074):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://bio-oge.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'география':

            list_ = []

            for i in range(960191, 960207):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://geo-oge.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'обществознание':

            list_ = []

            for i in range(2256504, 2256520):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://soc-oge.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'химия':

            list_ = []

            for i in range(1292933, 1292949):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://chem-oge.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'математика':
            list_ = []
            for i in range(21991234, 21991250):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == "информатика":
            list_ = []
            for i in range(8472777, 8472793):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://inf-oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'русский':
            list_ = []
            for i in range(4579017, 4579033):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://rus-oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == "физика":
            list_ = []
            for i in range(1801910, 1801925):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://phys-oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == "история":
            list_ = []
            for i in range(499904, 499920):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://hist-oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'английский':
            list_ = []
            for i in range(657557, 657573):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://en-oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'литература':
            list_ = []
            for i in range(124630, 124646):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://lit-oge.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        else:
            return "Нет такого предмета"
    except:
        return 'Ошибка'


def ege(text):
    try:
        subject = text.split(' ')[0]
        var = int(text.split(' ')[1])
        if subject.lower() == 'химия':

            list_ = []

            for i in range(3062442, 3062458):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://chem-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'биология':

            list_ = []

            for i in range(3032216, 3032232):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://bio-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'география':
            list_ = []
            for i in range(482724, 482740):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://geo-ege.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == "обществознание":
            list_ = []
            for i in range(5001765, 5001781):
                list_.append(i)
            var_ = str(list_[var])  # номер варианта на сайте
            url_ = "https://soc-ege.sdamgia.ru/test?id=" + var_ + "&print=true"
            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        elif subject.lower() == 'математика':

            list_ = []

            for i in range(25548590, 25548606):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://math-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'информатика':

            list_ = []

            for i in range(5445850, 5445866):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://inf-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'русский':

            list_ = []

            for i in range(13838728, 13838744):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://rus-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'английский':

            list_ = []

            for i in range(1009030, 1009046):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://en-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'физика':

            list_ = []

            for i in range(5159324, 5159340):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://phys-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == 'литература':

            list_ = []

            for i in range(843053, 843069):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://lit-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']

        elif subject.lower() == "история":

            list_ = []

            for i in range(2488328, 2488344):
                list_.append(i)

            var_ = str(list_[var])  # номер варианта на сайте

            url_ = "https://hist-ege.sdamgia.ru/test?id=" + var_ + "&print=true"

            req = requests.get(url_)
            soup = bs(req.text, 'html.parser')
            pdf = soup.find('a', id='pdf_linkh')
            return pdf['href']
        else:
            return 'Нет такого предмета'
    except:
        return 'Ошибка'
