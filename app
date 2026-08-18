class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"


my_dog = Dog("Buddy", "Golden Retriever")

print(f"My dog's name is {my_dog.name}.")
print(my_dog.speak())

 Output:
 My dog's name is Buddy.
 Buddy the Golden Retriever says Woof!
