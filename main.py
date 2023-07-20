import pyperclip as pc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def check_data():
    with open('data.txt', 'r', encoding='cp1251') as f:
        lines = []
        for i in f.readlines():
            if i != "\n":
                lines.append(i)
    data = []
    n = 100
    for i in range(0, len(lines), n):
        data.append(lines[i:i + n])
    return data


def start_script(region, url, data, browser):
    browser.get('https://be1.ru/position-yandex-google/')

    input_field_region = browser.find_element(By.NAME, 'region')
    select = Select(input_field_region)
    select.select_by_visible_text(region)

    input_field_url = browser.find_element(By.NAME, 'url')
    input_field_url.send_keys(url)

    pc.copy(''.join(data))
    input_field_data = browser.find_element(By.NAME, 'queries')
    input_field_data.send_keys(Keys.CONTROL, 'v')

    submit_button = browser.find_element(By.ID, 'tool-form-btn')
    submit_button.click()
    return


def main():
    region = "Екатеринбург"
    url = "https://akva-ural.ru/"
    with webdriver.Chrome() as browser:
        for data_chunk in check_data():
            start_script(region, url, data_chunk, browser)
    print("\nРабота завершена")
    pc.copy('')
    return


if __name__ == "__main__":
    main()
