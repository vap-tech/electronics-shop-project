from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Apple Keyboard', 3200, 7)

    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
