class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} drink water")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog=Dog("tiger")
cat=Cat("mimi")
mouse=Mouse("titi")

print(dog.name)
dog.eat()
cat.drink()
mouse.sleep()