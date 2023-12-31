from config import DATA_DIR
import json


def get_data():
    """
    Функция извлекает данные из файла operations.json и преобразует
    из формата json в читаемый код
    :return: возвращает список словарей
    """
    with open(DATA_DIR, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    return data


def split_text_numbers(bill):
    """
    Функция превращает строку счета в список из названия счета и его номера
    :param bill: данные счета в виде одной строки
    :return: возвращаем список состоящий из двух элементов: названия счета или карты и его номера
    """
    text = ""
    numbers = ""
    res = []
    for i in bill:
        if i.isdigit():
            numbers += i
        else:
            text += i
    res.append(text.strip())
    res.append(numbers)
    return res


def encrypt_bill_num(bill_num):
    """
    Функция, определяющая счет это или карта
    :param bill_num: номер карты или счета
    :return: возвращает только цифры карты или счета
    """
    if len(bill_num) == 20:
        return f'**{bill_num[-4:]}'
    elif len(bill_num) == 16:
        return f'{bill_num[:4]} {bill_num[4:6]}** **** {bill_num[-4:]}'
