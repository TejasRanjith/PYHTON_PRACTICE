class Animal():
    def __init__(self):
        print("Animal Created.")

    def who_am_i(self):
        print("I am an Animal.")

    def eat(self):
        print("I am Eating.")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
