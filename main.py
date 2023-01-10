import os
import random
from datetime import datetime, timedelta, timezone

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
        if every:
            future_in_half_hour = datetime.now(timezone.utc) + timedelta(minutes=3)
        else:
            rand_minutes = random.randint(2, 3)

            future_in_half_hour = datetime.now(timezone.utc) + timedelta(minutes=rand_minutes)

        local_time = future_in_half_hour.astimezone()

        pywhatkit.sendwhatmsg(f"+{element}", text_sms, local_time.time().hour,
                              local_time.time().minute, tab_close=True, close_time=3)


if __name__ == '__main__':
    every_minute = input('Отправка каждые 3 минуты? (y - да/n - случайное кол-во минут) ').lower()

    if every_minute not in ['y', 'n']:
        print('Введено неверное значение')
    else:
        buf = True if every_minute.lower() == 'y' else False

        phones = get_list_phone()
        text = get_text_msg()

        if text is None or phones is None:
            print('ERROR!')
        else:
            send_msg(phones, text, buf)
