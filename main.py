import datetime
import os
import random

import pywhatkit


def get_list_phone():
    buf = None

    try:
        with open(f'{os.getcwd()}/db.txt', mode='r', encoding='utf-8') as file:
            buf = file.readlines()

        index = 0
        for el in buf:
            buf[index] = el.replace('https://wa.me/', '').replace('?text=', '').replace('\n', '')
            index += 1
    except FileNotFoundError:
        print('Не найден файл с номерами! Проверьте, что есть файл db.txt в этой папке!')

    return buf


def get_text_msg():
    buf = None

    try:
        with open(f'{os.getcwd()}/text.txt', mode='r', encoding='utf-8') as file:
            buf = file.read()
    except FileNotFoundError:
        print('Не найден файл с номерами! Проверьте, что есть файл text.txt в этой папке!')

    return buf


def send_msg(phones_list, text_sms, every=True):
    for element in phones_list:
        today = datetime.datetime.now()

        hour = 0 if today.minute == 57 and today.hour == 23 else today.hour
        minute = today.minute

        if every:
            minute = minute + 2 if minute < 57 else 0
        else:
            minute = random.randint(minute, 57) if minute < 57 else random.randint(1, 3)


        pywhatkit.sendwhatmsg(f"+{element}", text_sms, hour, minute, tab_close=True, close_time=3)


if __name__ == '__main__':
    every_minute = input('Отправка каждые 3 минуты? (y - да/n - в случайное кол-во минут) ').lower()

    if every_minute not in ['y', 'n']:
        print('Введено неверное значение')
    else:
        every_minute = True if every_minute.lower() == 'y' else False

        phones = get_list_phone()
        text = get_text_msg()

        if text is None or phones is None:
            print('ERROR!')
        else:
            send_msg(phones, 'Hi', every_minute)
