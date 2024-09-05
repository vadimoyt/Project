def simple(num):
    d = 2
    while num % d != 0:
        d += 1
    return  d == num
num = int(input())
a = simple(num)
print(a)











