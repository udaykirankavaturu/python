class FirstClass():
    def __init__(self, name):
        self.name = name

    def firstMethod(self):
        print(self)


firstObject = FirstClass('uday')
firstObject.firstMethod()
