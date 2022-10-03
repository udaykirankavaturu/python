class User:
    def anyMethod(self):
        print('hello')


class Elves(User):
    pass


elves1 = Elves()
elves1.anyMethod()
