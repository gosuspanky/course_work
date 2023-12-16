from src.classes import Operation
from src.utils import get_data


def main():
    # получаем данные из файла
    data = get_data()
    executed_operations = []

    # переносим в новый список все данные операций, кроме непрошедших (отмененных)
    for i in range(len(data)):
        if data[i] == {}:
            continue

        if data[i]["state"] == "EXECUTED":
            executed_operations.append(data[i])
        else:
            continue

    # Забираем последние 5 операций по переводам средств
    new_operations = executed_operations[-5:]

    # запускаем обратный цикл и выводим на экран данные, соответствующие заданию
    for i in range(len(new_operations) - 1, -1, -1):
        operation = Operation(new_operations[i])

        date = operation.get_date()
        description = new_operations[i]["description"]
        amount = new_operations[i]["operationAmount"]["amount"]
        currency_name = new_operations[i]["operationAmount"]["currency"]["name"]

        if "from" in new_operations[i]:

            sender = operation.encrypt_bill()[0]
            receiver = operation.encrypt_bill()[1]

            print(f'{date} {description}\n'
                  f'{sender} -> {receiver}\n'
                  f'{amount} {currency_name}\n')
        else:

            receiver = operation.encrypt_bill()[1]

            print(f'{date} {description}\n'
                  f'{receiver}\n'
                  f'{amount} {currency_name}\n')


if __name__ == '__main__':
    main()
