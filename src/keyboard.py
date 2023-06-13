from src.item import Item


class MixinLang:
    langs = ['EN', 'RU']

    def __init__(self):
        self.__lang = 0

    @property
    def language(self):
        return self.langs[self.__lang]

    def change_lang(self):
        self.__lang = not self.__lang
        return self


class Keyboard(Item, MixinLang):
    pass
