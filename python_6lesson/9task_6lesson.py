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
v = []
for i in a:
    v.append(sum(i))
print('Сумма всех элементов', sum(v))
sum = 0
perc = []
for col_ind in range(len(a)):
     col_sum = 0
     for row in a:
         col_sum += row[col_ind]
     sum += col_sum
     perc.append(col_sum)
print(sum)
print(perc)
for i, percent in enumerate(perc):
    perc[i] = f"{percent / sum * 100:.2f}"
    print(perc[i])










