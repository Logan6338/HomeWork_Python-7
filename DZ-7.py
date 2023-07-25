import os
import random as rd
from itertools import cycle
from pathlib import Path
from works_file import sort_file

'''
Задание №1
✔ Напишите функцию, которая заполняет файл 
(добавляет в конец) случайными парами чисел. 
✔ Первое число int, второе - float разделены вертикальной чертой. 
✔ Минимальное число - -1000, максимальное - +1000. 
✔ Количество строк и имя файла передаются как аргументы функции. 
'''


def task_1(number_row: int, file_name: str) -> None:
    RANGE_NUMBER = 1000
    with open(f'{file_name}', 'a', encoding='utf-8') as file:
        for _ in range(number_row):
            file.write(
                f'{rd.randint(-RANGE_NUMBER, RANGE_NUMBER)} | {rd.uniform(float(-RANGE_NUMBER), float(RANGE_NUMBER)):.2f}\n')


'''
Задание №2
✔ Напишите функцию, которая генерирует 
псевдоимена. 
✔ Имя должно начинаться с заглавной буквы, 
состоять из 4-7 букв, среди которых 
обязательно должны быть гласные. 
✔ Полученные имена сохраните в файл.
'''


def task_2(file_name=0, min_number_name=6, max_number_name=7) -> None | str:
    VOWELS = 'AEIOU'.lower()
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    if file_name:
        with open(f'{file_name}', 'a', encoding='utf-8') as file:
            new_name_file = f'{rd.choice(VOWELS)}'
            for _ in range(1, rd.randint(min_number_name, max_number_name)):
                new_name_file += rd.choice(ALPHABET)
            file.write(f'{new_name_file.capitalize()}\n')
    else:
        new_name_file = f'{rd.choice(VOWELS)}'
        for _ in range(1, rd.randint(min_number_name, max_number_name)):
            new_name_file += rd.choice(ALPHABET)
        return new_name_file


'''
Напишите функцию, которая открывает на чтение созданные 
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните 
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя 
записанное строчными буквами и произведение по модулю   # маленькие буквы
✔ если результат умножения положительный, сохраните имя 
прописными буквами и произведение округлённое до целого. # Большие буквы
✔ В результирующем файле должно быть столько же строк, 
сколько в более длинном файле. 
✔ При достижении конца более короткого файла, 
возвращайтесь в его начало.
'''


def task_3(first_file_name: str, second_file_name: str) -> None:
    with (
        open(f'{first_file_name}', 'r', encoding='utf-8') as first_file,
        open(f'{second_file_name}', 'r', encoding='utf-8') as second_file,
        open(f'test_lesson_7\\rezul.txt', 'a', encoding='utf-8') as rezul
    ):
        name_list = list(
            map(lambda x: x.replace('\n', ''), first_file.readlines()))
        number_list = list(map(lambda x: x.split('|'), second_file.readlines()))
        rezul_num = [int(y) * float(x.replace('\n', '')) for (y, x) in
                     number_list]
        if len(number_list) >= len(name_list):
            rezul_ = list(zip(rezul_num, cycle(name_list)))
            for (y, x) in rezul_:
                if y > 0:
                    rezul.write(f'{x.upper()}:{int(y)}\n')
                else:
                    rezul.write(f'{x.lower()}:{abs(y)}\n')
        else:
            rezul_ = list(zip(name_list, cycle(rezul_num)))
            for (y, x) in rezul_:
                if x > 0:
                    rezul.write(f'{y.upper()}:{int(x)}\n')
                else:
                    rezul.write(f'{y.lower()}:{abs(x)}\n')


'''
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением. 
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''


def task_4(expansion='txt', min_name=6, max_name=30, min_byte=256,
           max_byte=4096, count_file=42) -> None:
    byte = rd.randint(min_byte, max_byte)
    for _ in range(count_file):
        name = task_2(0, min_name, max_name)
        with open(f'{name}.{expansion}', 'xb') as f:
            f.write(os.urandom(byte))


'''
Задание №5
✔ Доработаем предыдущую задачу. 
✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
✔ Расширения и количество файлов функция принимает в качестве параметров. 
✔ Количество переданных расширений может быть любым. 
✔ Количество файлов для каждого расширения различно. 
✔ Внутри используйте вызов функции из прошлой задачи.
'''
'''
Задание №6
✔ Дорабатываем функции из предыдущих задач. 
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции. 
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции 
(добавьте проверки). 
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''


def task_5(expansions: list[str], count_file: int, directory=Path().cwd()):
    end_file_name = [rd.choice(expansions) for _ in range(count_file)]
    if Path(directory).is_dir():
        os.chdir(directory)
    else:
        directory = Path().cwd() / directory
        Path(directory).mkdir(parents=True)
        os.chdir(directory)
        print(directory)
    for x in end_file_name:
        try:
            task_4(x, count_file=1)
        except FileExistsError:
            print(f'Данное имя уже зарезервировано')


'''
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
✔ Каждая группа включает файлы с несколькими расширениями. 
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''


def task_7(directory: str) -> None:
    extensions = {
        'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg',
                  'mpeg', 'm4v',
                  'h264', 'flv', 'rm', 'swf', 'vob'],

        'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb',
                 'sav',
                 'tar', 'xml'],

        'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa',
                  'wma', 'wpl',
                  'cda'],

        'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg',
                  'tif',
                  'tiff'],
        'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

        'exe': ['exe'],
    }
    if not Path(directory).is_dir():
        directory = Path().cwd() / directory
        Path(directory).mkdir(parents=True)
        task_5(['txt', 'mp4', 'mov', 'avi', 'sqlite', 'sqlite3', 'csv', 'dat',
                'mp3', 'wav', 'ogg', 'pdf', 'txt', 'doc', 'docx'], 15,
               directory)

    rezul = [file.split('.') for dirs, folders, files in os.walk(directory) for
             file in files]

    for (name, expan) in rezul:
        for k, v in extensions.items():
            if expan in v:
                new_dir = Path().cwd() / directory / k
                if new_dir.is_dir():
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')
                else:
                    Path(new_dir).mkdir(parents=True)
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')


'''old_file = Path(old_name)
    new_file = old_file.replace(Path().cwd() / folder / old_file)
    такая конструкция перемещает в ново - созданное  представление директории с помощью (Path().cwd() / folder  / old_file)'''

'''
Задание
✔ Решить задачи, которые не успели решить на семинаре. +
✔ Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов. +
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона 
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется 
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''


def home(end_name: str, count_sequence_number: int, start_expansions: str,
         end_expansions: str, slice_name: list[int, int],
         directory=Path().cwd()):
    start_number = 1
    start_slice, end_slace = slice_name
    for dirs, folders, files in os.walk(directory):
        for i, file in enumerate(files):
            if file.endswith(start_expansions):
                old_name = Path(dirs) / file
                old_name.rename(
                    f'{dirs}\{file[start_slice:end_slace]}{end_name}{str(start_number).zfill(count_sequence_number)}.{end_expansions}')
                start_number += 1


if __name__ == '__main__':
    # task_5(['txt','mp4', 'mov', 'avi','sqlite', 'sqlite3', 'csv', 'dat','mp3', 'wav', 'ogg','pdf', 'txt', 'doc', 'docx'],15,'Test_folder_file')
    # task_4('txt',6,6,count_file=1)
    # task_3('test_lesson_7\\task_2.txt','test_lesson_7\\task_1.txt')
    # print(os.path.getsize("afkpvvuwatwihhawpsadppib.txt"))
    # task_1(3,'test_lesson_7\\task_1.txt')
    # home('файл',3,'txt','dat',[0,2],'Test_folder_file')
    # sort_file.sorted_file('Test_folder_file')
    # sort_file.sorted_file('Test_folder_file')
    # task_7('Test_folder_file')
    pass