number = int(input())

def infinite_sequence(number):
    while True:
        yield 1
        yield 2
        yield 3


infinite_sequence = infinite_sequence(10)
for n, i in zip(range(number), infinite_sequence):
    print(i)




