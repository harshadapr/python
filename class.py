class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(f"{dog1.name} is a {dog1.breed} and says {dog1.bark()}")
print(f"{dog2.name} is a {dog2.breed} and says {dog2.bark()}")
