from operator import index
from random import randint

def create_random_array(m,n):
    a = []
    for i in range (m):
        new_row = []
        for j in range(n):
            new_row.append(randint(0,1))
        a.append(new_row)
    return(a)
m = 3
n = 3
a = create_random_array(m,n)
for i in a:
    print(i)

for r in a:
    r.append((sum(r) / 2))
for n in a:
    print(n)







