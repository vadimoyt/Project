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
main = 0
second = 0
for i in range(m):
    main += a[i][i]
    second += a[i][m - i - 1]
print(main)
print(second)








