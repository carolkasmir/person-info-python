class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# creating a Person class instance using the provided information
person1 = Person("Carolyne", 35, "Female")

# Calling the introduce method
person1.introduce()
