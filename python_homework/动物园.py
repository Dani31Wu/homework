# User: link
# Date: 2023/9/9
# File: 动物园

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def call(self):
        print("dog call")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def call(self):
        print("cat call")


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def call(self):
        print("bird call")


dog = Dog('小狗', 1)
cat = Cat('小猫', 2)
bird = Bird('小鸟', 3)

dog.call()
cat.call()
bird.call()