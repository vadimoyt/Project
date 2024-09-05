import os
import re

from idlelib.replace import replace

path = os.path.join('TextFiles', 'new_file.txt')
with open (path, "r+") as text:
    text_ = text.read()
    new_text = re.sub(r"(.[А-Я][а-я]+){3,4}", ' N', text_)
    print('*****',new_text, '*****')
    text.write('\n' + new_text)

