class Person:
    def __init__(self, first_name, last_name, age, department, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.gpa = gpa
    def get_full_name(self):
        return self.first_name + " " + self.last_name


def print_name():
    person1 = Person("Sintayehu", "Fantaye", 23, "CS", 3.98)
    full_name = person1.get_full_name()

    print(full_name)


print_name()