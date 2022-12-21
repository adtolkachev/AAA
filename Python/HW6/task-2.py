import sys
from datetime import datetime


def timed_output(function):
    """Добавляем к выводу текущее время"""
    def wrapper(some_text):
        current_datetime = str(datetime.now().replace(microsecond=0))
        sys.stdout.write(f'[{current_datetime}]: ')
        return function(some_text)
    return wrapper


@timed_output
def print_greeting(name):
    """Приветствие с информацией о текущем времени"""
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting('Nikita')
