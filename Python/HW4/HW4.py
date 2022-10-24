import json
from keyword import iskeyword
from typing import Dict


class ColorizeMixin:

    """
    Миксин, который позволяет покрасить вывод в консоль в прикольный цвет
    """

    def __init__(self, color):
        """
        Конструктор
        """
        self.color = color

    def __str__(self):
        """
        Строковой вывод, заменяющий цвет вывода сообщением в консоль
        """
        return f'\033[1;{self.color}m' + self.__repr__()


class Advert(ColorizeMixin):

    '''Создает объект класса из словаря с возможностью обращения
    к атрибутам через точку.'''

    def __init__(self, mapping: Dict, color=0):
        """
        Конструктор
        """
        super().__init__(color)
        advert_mapper = AdvertMapper(mapping).__dict__
        if advert_mapper.get('price', 0) < 0:
            raise ValueError('Цена должна быть больше нуля!\
                (Ошибка на этапе чтения исходного словаря)')
        self.__dict__.update(advert_mapper)

    def __repr__(self) -> str:
        """
        Строковой вывод при обращении к экземпляру класса,
        учитывает цветовой код
        """
        return f'{self.title} | {self.price} рублей'

    @property
    def price(self):
        """
        Геттер для цены - устанавливает 0 если цены нет в джейсоне
        """
        return self.__dict__.get('price', 0)

    @price.setter
    def price(self, set_price):
        """
        Сеттер для цены - проверяет, вводится ли цена больше нуля
        """
        if set_price < 0:
            raise ValueError('Цена должна быть больше нуля!\
            (ошибка на этапе присвоения цены)')
        # self.price = set_price


class AdvertMapper:

    '''Класс создает питонячий объект из JSON.
    Вложенные словари распаршиваются как экземпляры этого же класса.'''

    def __init__(self, json_dict):
        """
        Конструктор
        """
        for key, value in json_dict.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = AdvertMapper(value)
            else:
                self.__dict__[key] = value

    def __str__(self):
        """
        Строковой вывод при обращении к экземпляру класса
        """
        return f'{self.__dict__}'


if __name__ == '__main__':

    lesson_json = """{
        "title": "python",
        "price": 0,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
                }
    }"""
    lesson_dict = json.loads(lesson_json)

    iphone_json = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    iphone_dict = json.loads(iphone_json)

    corgi_json = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
        "address": "сельское поселение Ельдигинское,\
        поселок санатория Тишково, 25"
        }
    }"""
    corgi_dict = json.loads(corgi_json)

    lesson = Advert(lesson_dict)
    iphone = Advert(iphone_dict)
    corgi = Advert(corgi_dict)

    print(lesson, iphone, corgi, sep='\n')

    try:
        lesson.price = -200
    except ValueError as error:
        print(str(error))

    yellow_corgi = Advert(corgi_dict, color=33)
    print(yellow_corgi)
    print(yellow_corgi.location.address)