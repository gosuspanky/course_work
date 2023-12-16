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
