from turtledemo.nim import NimView


class Soda:

    def __init__(self, kind=None):
        self.kind = kind

    def dispaly_info(self):
        if self.kind:
            print(f"У вас газировка с {self.kind} вкусом")
        else:
                print("У вас обычная газировка")


banana_soda = Soda()
banana_soda.dispaly_info()

banana_soda = Soda(kind="банановым")
banana_soda.dispaly_info()

