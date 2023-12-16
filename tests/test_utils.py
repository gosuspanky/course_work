from src.utils import get_data


def test_get_data():
    assert type(get_data()) == list
    assert type(get_data()[1]) == dict
