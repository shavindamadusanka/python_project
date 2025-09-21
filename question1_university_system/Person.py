class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def change_age(self, new_age):
        self.age = new_age

    def change_name(self, name):
        self.name = name

    def get_responsibilities(self):
        return "General responsibilities"