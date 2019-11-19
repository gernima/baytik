from selenium import webdriver

chromedriver_path = 'chromedriver.exe'


def click_hm(login, password, message, bot, keyboard):
    try:
        login, password = message.text.split(' ')
        print(login, password)
        dz = parsing(login, password)
        bot.send_message(message.chat.id, dz, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, "Неверный логин или пароль или edu.tatar не доступен в вашей стране")


def parsing(login, password):
    driver = webdriver.Chrome(chromedriver_path)

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
