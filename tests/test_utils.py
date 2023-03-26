from utils import date, hide, format


def test_date():
    assert date('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert date('2018-11-29T07:18:23.941293') == '29.11.2018'


def test_hide():
    assert hide('MasterCard 3152479541115065') == 'MasterCard 3152 47** **** 5065'
    assert hide('Счет 43597928997568165086') == 'Счет **5086'


def test_format():
    data = {
    "id": 633268359,
    "state": "EXECUTED",
    "date": "2019-07-12T08:11:47.735774",
    "operationAmount": {
      "amount": "2631.44",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 3589276410671603",
    "to": "Счет 96292138399386853355"
  }
    result = '12.07.2019 Перевод организации\nVisa Gold 3589 27** **** 1603 -> Счет **3355\n2631.44 руб.'
    assert format(data) == result
