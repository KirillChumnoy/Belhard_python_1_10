"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows(file_path: str):
    revert_text = ''
    with open(file_path, 'r') as file:
        for line in file:
            list_line = list(line.split())
            revert_line = ' '.join(list_line[::-1])
            revert_text += revert_line + '\n'

    with open('revert_text.txt', 'w') as revert_file:
        revert_file.writelines(revert_text)


revert_rows('text.txt')
