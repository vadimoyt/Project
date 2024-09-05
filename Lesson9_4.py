import re

with open ('les9_censore.txt', 'r+') as censore:
        text = censore.read()
        print(text)
with open ('stop_words.txt', 'r+') as stop:
        stop_w = stop.read()
        sp = stop_w.split(' ')
def new(sp, text):
        censored_text = text
        for word in sp:
                censored_text = re.sub(word, '*'*len(word), censored_text, flags=re.I|re.M)
        return censored_text
print(new(sp, text))
