import os
import shutil
from os import listdir

print('имя ОС', os.name)
print('Путь к текущей папке', os.getcwd())
try:
    os.mkdir('TextFiles')
except FileExistsError:
    pass
try:
    os.mkdir('HtmlFiles')
except FileExistsError:
    pass
files = os.listdir(os.getcwd())
ls_of_txt_files = []
size_of_txt_files = 0
ls_of_html_files = []
size_of_html_files = 0
for file in files:
    type_of_files = file.split('.')
    if len(type_of_files) > 1:
        if 'html' in type_of_files:
            ls_of_html_files.append(file)
            size = os.path.getsize(file)
            size_of_html_files += size
        elif 'txt' in type_of_files:
            ls_of_txt_files.append(file)
            size = os.path.getsize(file)
            size_of_txt_files += size
print(f"Будет перемещено {len(ls_of_html_files)} html файла/ов, общим размеров {size_of_html_files} байт")
print(f"Будет перемещено {len(ls_of_txt_files)} txt файла/ов, общим размеров {size_of_txt_files} байт")
for file in ls_of_html_files:
    shutil.move(os.path.join(file), os.path.join('HtmlFiles'))
for file in ls_of_txt_files:
    shutil.move(os.path.join(file), os.path.join('TextFiles'))

try:
    path_to_file = os.path.join('TextFiles', '2223.txt')
    file = os.path.basename(path_to_file)
    text= f'файл был переименован c {file} нa '
    os.replace(os.path.join('TextFiles', '2223.txt'), os.path.join('TextFiles', 'new_file.txt'))
    path_to_renamed_file = os.path.join('TextFiles', 'new_file.txt')
    renamed_file = os.path.basename(path_to_renamed_file)
    text1= f'{renamed_file}'
    text2 = f'{text + text1}'
    print(text2)
except FileNotFoundError:
    pass


