import sys
from task_1 import my_write


def timed_output(function: callable) -> callable:
    """Добавляем к выводу текущее время"""

    original_write = sys.stdout.write

    def wrapper(*args, **kwargs) -> callable:
        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result
 
    return wrapper


@timed_output
def print_greeting(name):
    """Приветствие с информацией о текущем времени"""
    print(f'Hello, {name}')


if __name__ == '__main__':
    print_greeting('Nikita')
