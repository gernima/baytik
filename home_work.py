from selenium import webdriver

chromedriver_path = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("disable-gpu")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
prefs = {'profile.managed_default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
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

caps = webdriver.DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"  # eager - 32 sec normal - 50 sec


def click_hm(login, password, message, bot, keyboard):
    try:
        # login, password = message.text.split(' ')
        print(login, password)
        dz = parsing(login, password)
        bot.send_message(message.chat.id, dz, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, "Неверный логин пароль или edu.tatar не доступен в вашей стране")


def parsing(login, password):  # local - 33 sec
    driver = webdriver.Chrome(chromedriver_path, desired_capabilities=caps, chrome_options=options)

    driver.get('https://edu.tatar.ru/logon')

    login_input = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/form/div[4]/input[1]')
    login_input.send_keys(login)

    pass_input = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/form/div[4]/input[2]')
    pass_input.send_keys(password)

    login_buttom = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/form/div[4]/div/button')
    login_buttom.click()

    driver.get('https://edu.tatar.ru/user/diary/day')

    next_day_button = driver.find_element_by_xpath(
        '//*[@id="content"]/div[2]/div/div/div[2]/table/tbody/tr/td[3]/span/a')
    next_day_button.click()

    day_table = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[3]/table/tbody')

    day_subjects = day_table.find_elements_by_tag_name('tr')

    day_subjects = [subject.text.split('\n') for subject in day_subjects]
    day_subjects = [
        s[0] + s[1] + s[2].split(' ')[0] + ' | ' + s[2].split(' ')[1] + (' | ' + s[3] if len(s) == 4 else '')
        for s in day_subjects]

    homework = '\n'.join(day_subjects)

    driver.quit()

    return homework
