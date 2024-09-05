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
m = int(input())
n = int(input())
a = create_random_array(m,n)
for i in a:
    print(i)






