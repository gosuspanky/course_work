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


def test_new_time():
    assert operation.new_time() == "14.10.2018"


def test_encrypt_bill():
    assert operation.encrypt_bill() == ("Visa Platinum 2256 48** **** 2539", "Счет **9319")
