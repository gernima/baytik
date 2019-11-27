from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver

# ! /usr/bin/env python
# -*- coding: utf-8 -*-


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("disable-gpu")
options.add_argument("--disable-extensions")
prefs = {'profile.managed_default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 0,
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2,
                                                            'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2, 'push_messaging': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2},
         "profile.managed_default_content_settings.images": 2}

options.add_experimental_option("prefs", prefs)


def get_gdz(what):
    try:
        base = 'https://gdz.ru/search/?q='
        driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        q = '+'.join(what.lower().split(' '))
        url = base + q
        driver.get(url)
        html = driver.page_source
        soup = bs(html, 'html.parser')
        a = soup.find("a", class_='gs-title')
        new_url = a['href']
        driver.get(new_url)
        html = driver.page_source
        driver.quit()
        soup = bs(html, 'html.parser')
        photo = soup.find('div', class_='with-overtask').find('img')
        src_photo = photo['src'][2:]
        return src_photo
    except:
        return 'Ошибка'
