from audioop import reverse
number = int(input())
sp = []
while number > 0:
    sp.append(number % 2)
    number //= 2
sp.reverse()
for i in sp:
    print(i, end='')











