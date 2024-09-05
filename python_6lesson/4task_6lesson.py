def simple(num1, num2):
    sp =[]
    if num1 > num2:
        for i in range(1, num1):
            if num1 % i == 0 and num2 % i == 0:
                sp.append(i)
    elif num1 < num2:
        for i in range(1, num2):
            if num1 % i == 0 and num2 % i == 0:
                sp.append(i)
    return max(sp)
num1 = int(input())
num2 = int(input())
a = simple(num1, num2)
print(a)











