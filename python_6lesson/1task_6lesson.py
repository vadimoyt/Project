def search(lst, low, high, elem):
    if high < low:
        return None
    else:
        guess = (low + high) // 2
        if lst[guess] > elem:
            iskomoe = search(lst, low, guess - 1, elem)
            return iskomoe
        elif lst[guess] < elem:
            iskomoe = search(lst, guess + 1, high, elem)
            return iskomoe
        else:
            return guess
lst = sorted([2, 5, 3, 10, 1023, 203])
elem = int(input('Введите число'))
print(search(lst, 0, len(lst), elem))
print(lst)





