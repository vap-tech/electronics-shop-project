import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self) -> str:
        return f'''{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})'''

    def __str__(self) -> str:
        return str(self.name)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """инициализирует экземпляры `Item` данными из файла _src/items.csv_"""
        file_path = os.path.join('..', 'src', 'items.csv')
        if not os.path.exists(file_path):
            file_path = os.path.join('src', 'items.csv')  # Если запускаемся на уровень выше...
        with open(file_path, encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string: str) -> int:
        if string.isdigit():
            return int(string)
        return int(float(string))
