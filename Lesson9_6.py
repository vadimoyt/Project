import re

with open('nabor_symbols.txt', 'r+') as nabor:
        stroka = nabor.read()
        numbers = re.findall(r"[0-9]+", stroka)
        sum = 0
        for i in numbers:
                sum += int(i)
        print(sum)
