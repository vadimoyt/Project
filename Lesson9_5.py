with open('marks.txt', 'r+') as marks:
        a = marks.readlines()
        for i in a:
                for c in list(range(1, 4)):
                        if str(c) in i.split():
                                print(i)

