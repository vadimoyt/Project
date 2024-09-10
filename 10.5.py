from cmath import isinf


class SuperStr:

    def __init__(self, stroka=None):
        self.stroka = stroka
        if stroka is None:
            self.stroka = ''

    def is_repeatance(self, s):
        if s not in self.stroka:
            return False
        n = len(self.stroka) // len(s)
        return self.stroka == n * s


    def is_palindrom(self):
        return True if list(reversed(self.stroka)) == list(self.stroka) else False

stroka = SuperStr(stroka='шалашшалашшалаш')
print(stroka.is_palindrom())
print(stroka.is_repeatance('шалаш'))
