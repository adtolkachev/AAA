
import csv
from importlib.resources import path
from typing import DefaultDict
from collections import defaultdict
from venv import create

def initial_csv_parser(path: str = '/Users/aleksejtolkacev/AAA/Python/HW2/Corp_Summary.csv') -> list:

    """Эта функция читает csv файл и возвращает объект data -  лист из строк этого файла.
    Опциональный параметр path - позволяет указать путь к считываемому файлу. """

    with open(path, newline='') as csv_file:
        initial_file = csv.reader(csv_file, delimiter=';')
        data = []
        for index, employees in enumerate(initial_file): # получаем всю дату из таблицы, кроме заголовка, в форме тюпла из листов
            if index and employees:
                data.append(list(employees))
        
        return data

def hierarchy(data: list) -> DefaultDict[str, set]:
    """ Эта функция собирает данные, полученные в результате работы функции initial_csv_parser() в словарь
    из уникальных департаментов и отделов.
    Принимает на вход обязательный аргумент data: list - результат работы функции initial_csv_parser """

    hierarchy = defaultdict(set)

    for employee in data:
        department = employee[1]
        branch = employee[2]
        hierarchy[department].add(branch)

    return hierarchy


def print_hierarchy(hierarchy: DefaultDict[str, set]) -> None:

    """Функция печатает иерархию компании - принимает на вход словарь hierarchy из функции hierarchy и возвращает None"""
    
    for item in hierarchy:
        branch_count = len(hierarchy[item])
        print(f'Название департамента: {item}.\n', end='')
        print(f'В этом департаменте {branch_count} отдела:\n', end='')
        print('\n'.join(hierarchy[item]))
        print('')

def create_report(data: list)->list:
    """Эта функция принимает на вход лист с данными из initial_parser_csv и переупаковывает данные в лист с параметрами сводного отчета - словарями.
    Вовзвращает list"""
    firm_hierarchy = hierarchy(data).keys()
    departments = set()
    report = []
    for dept in firm_hierarchy:
        departments.add(dept)

    for dept in departments:
        dept_info = {}
        employees = []
        for row in data:
            if row[1] == dept:
                employees.append(row)
        salary_list = [int(row[-1]) for row in employees]
        sum_salary = 0
        for salary in salary_list:
            sum_salary += salary
        dept_info['Департамент'] = dept
        dept_info['Численность'] = len(employees)
        dept_info['Минимальная зарплата'] = min(salary_list)
        dept_info['Максимальная зарплата'] = max(salary_list)
        dept_info['Средняя зарплата'] = round(sum_salary / len(employees))
        report.append(dept_info)
    return report


def print_report(report: list)-> None:
    """Функция печатает сводный отчет компании - принимает на вход лист data из функции hierarchy и возвращает None"""

    print('\n')
    print('\n')
    print('Сводный отчет по департаментам компании:')
    print('\n')

    for dept in report:
        for key in dept.keys():
            print(f'{str(key)}: {dept[key]} ', end='\n')
            print('- - - - - - - - - - - - - - - -')
        print('_______________________________')
        print('\n')
    

def write_report_to_csv(report: list, output_path: str = '/Users/aleksejtolkacev/AAA/Python/HW2/output.csv')-> None:

    """Функция записывает отчет из функции create_report в формат .csv"""

    column_names = report[0].keys()
    with open(output_path, 'w', newline = '', encoding ='utf-8') as output:
        data_writer = csv.DictWriter(output, column_names, delimiter=';')
        data_writer.writeheader()
        data_writer.writerows(report)
        print(f'Файл сохранен в директорию {output_path}')

def main_menu()-> None:

    """Основная функция - точка входа в приложение. 
    Выводит на экран список команд, принимает номер нужной команды и вызывает необходимые функции."""

    print("""Добро пожаловать в приложение по созданию сводного отчета из .csv-файла!
    Введите номер необходимой команды из предложенного списка:""", end='\n')

    data = initial_csv_parser()
    user_input = ''
    options_map = {
        1: '1. Вывести иерархию департаментов и отделов компании.',
        2: '2. Вывести сводный отчет по компании.',
        3: '3. Сохранить сводный отчет в формате csv.'
    }
    

    while user_input not in options_map:
        for value in options_map.values():
            print(value)
        try: 
            user_input = int(input())
        except:
            user_input = ''

    if user_input == 1:
        print('Иерархия компании:')
        dept_hierarchy = hierarchy(data)
        print_hierarchy(dept_hierarchy)

    if user_input == 2:
        report = create_report(data)
        print_report(report)

    if user_input == 3:
        report = create_report(data)
        write_report_to_csv(report)
        

    main_menu()



if __name__ == '__main__':
    main_menu()