from typing import Callable
from random import randint
import click


class Pizza:
    """ Класс пицца с описанием рецептов"""
    def __init__(self, name: str, size: str = 'L'):
        """Проверка имени пиццы, размер по умолчанию L"""
        name = name.capitalize()
        if name not in ['Margherita', 'Pepperoni', 'Hawaiian']:
            raise ValueError('Такой пиццы нет в наличии')
        if size not in ['L', 'XL']:
            raise ValueError('Размер должен быть L или XL')

        self.name = name
        self.size = size

        if name == 'Margherita':
            self.name += ' 🧀'
            self.recipe = dict.fromkeys(
                [self.name], ['tomato sauce', 'mozzarella', 'tomatoes']
            )

        if name == 'Pepperoni':
            self.name += ' 🍕'
            self.recipe = dict.fromkeys(
                [self.name], ['tomato sauce', 'mozzarella', 'pepperoni']
            )

        if name == 'Hawaiian':
            self.name += ' 🍍'
            self.recipe = dict.fromkeys(
                [self.name], ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
            )

    def dict(self):
        """Возвращает рецепт в виде строки"""
        recipe = ''
        for name, ingredients in self.recipe.items():
            recipe = f'{name}: ' + ', '.join(ingredient for ingredient in ingredients)
        return recipe

    def __str__(self):
        return f'{self.name} ({self.size})'

    def __eq__(self, other):
        """ Сравнение двух пицц """
        return self.size == other.size and self.name == other.name


def log(text: str) -> Callable:
    """Выводит время выполнения"""
    def wrapper(function: Callable) -> Callable:
        def decorator(*args, **kwargs):
            for pizza in args:
                print(pizza, end=' ')
            print(text.format(randint(5, 30)))
            function(*args, **kwargs)
        return decorator
    return wrapper


@log(': приготовили за {} минут!')
def bake(pizza: Pizza):
    """Готовит пиццу"""


@log(': 🛵 доставили за {} минут!')
def delivery(pizza: Pizza):
    """Доставляет пиццу"""


@log(': 🏠 забрали за {} минут!')
def pickup(pizza: Pizza):
    """Самовывоз"""


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Выводит меню"""
    pizzas = [Pizza('Margherita'), Pizza('Pepperoni'), Pizza('Hawaiian')]
    for pizza in pizzas:
        print(f'- {pizza.dict()}')
    print('Размер пиццы: L или XL')


@cli.command()
@click.argument('pizza')
@click.argument('size', default='L')
@click.option('--delivery', is_flag=True, default=False)
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    order_pizza = Pizza(pizza, size)
    print(order_pizza.__str__() + ':')
    if order_pizza.size == 'L':
        print('     Приготовили за 10 минут')
    else:
        print('     Приготовили за 20 минут')
    if delivery:
        print('     Доставили за 30 минут')


if __name__ == '__main__':
    cli()
