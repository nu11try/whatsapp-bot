import datetime
import os
import random

import pywhatkit


def get_list_phone():
    buf = None

    try:
        with open(f'{os.getcwd()}/db.txt') as file:
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
        with open(f'{os.getcwd()}/text.txt') as file:
            buf = file.read()
    except FileNotFoundError:
        print('Не найден файл с номерами! Проверьте, что есть файл text.txt в этой папке!')

    return buf


def send_msg(phones_list, text, every_minute=True):
    for el in phones_list:
        today = datetime.datetime.now()

        hour = today.hour
        minute = today.minute

        if every_minute:
            minute = minute + 1 if minute < 59 else 0
        else:
            minute = random.randint(minute, 59) if minute < 58 else random.randint(1, 3)

        hour = hour + 1 if hour < 23 else 0

        pywhatkit.sendwhatmsg(f"+{el}", text, hour, minute, tab_close=True, close_time=3)


if __name__ == '__main__':
    every_minute = input('Отправка каждую минуту? (y - да/n - в случайное кол-во минут) ').lower()

    print(every_minute not in ['y', 'n'])

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
