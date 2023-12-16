from src.classes import Operation

operation = Operation({
    "id": 542678139,
    "state": "EXECUTED",
    "date": "2018-10-14T22:27:25.205631",
    "operationAmount": {
        "amount": "90582.51",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 2256483756542539",
    "to": "Счет 78808375133947439319"
})

second_operation = Operation({
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 35737585785074382265"
  })


def test_new_time():
    assert operation.get_date() == "14.10.2018"


def test_encrypt_bill():
    assert operation.encrypt_bill() == ("Visa Platinum 2256 48** **** 2539", "Счет **9319")
    assert second_operation.encrypt_bill() == ('', "Счет **2265")
