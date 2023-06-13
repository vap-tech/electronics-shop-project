import pytest
from src.item import Item
from src.phone import Phone


def test_phone():

    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert not phone1 + 3

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
