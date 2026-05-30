# Passing attributes and methods from one class to another
class Animal:
    def sleep(self):
        print("Sleeping...")

class Cat(Animal):
    def meow(self):
        print("Meow!")

my_cat = Cat()
my_cat.sleep()
my_cat.meow()