from Person import Person


class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")

    def get_responsibilities(self):
        return "Administrative support, manage records"