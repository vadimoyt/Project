from operator import index
from random import randint

def create_random_array(m,n):
    a = []
    for i in range (m):
        new_row = []
        for j in range(n):
            new_row.append(randint(-50,50))
        a.append(new_row)
    return(a)
m = 3
n = 3
a = create_random_array(m,n)
for i in a:
    print(i)
max_value = max(max(a, key=max))
min_value = min(min(a, key=min))
l = int(input)
for i in a:
    if l in i:
        print('Значение находится в столбце №', i.index(l))








