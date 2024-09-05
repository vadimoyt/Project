from collections import Counter



with open('text.txt') as text:
    stroki = text.readlines()
    spisok_max_value = []
    for word in stroki:
        spl_word = word.split(' ')
        max_value =  Counter(spl_word).most_common(1)
        spisok_max_value.append(max_value)
    print(spisok_max_value)
    new_file = open('NewFile.txt', 'w+')
    new_file.write(str(spisok_max_value))