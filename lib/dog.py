#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed = 'Mutt'):
        self.name = name
        self.breed = breed
dog1 = Dog("chocky","pomerian")
print(dog1.name)
print(dog1.breed)

dog2 = Dog("cookie","bulldog")
print(dog2.name)
print(dog2.breed)

dog3 = Dog("Lucy")
print(dog3.name)
print(dog3.breed)