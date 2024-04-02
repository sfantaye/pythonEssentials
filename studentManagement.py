class Student:
    def __init__(self, student_id, first_name, last_name, age, address):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def get_name(self):
        return self.first_name + " " + self.last_name


def generate_id(last_name):
    part_of_last_name = last_name[0:3]
    return part_of_last_name


def register():
    print("Enter student Information")
    print("-------------------------")

    roster = []
    flag = True

    roster = []
    flag = True
    attachment = 101

    while flag:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        address = input("Address: ")

        student_id = generate_id(last_name) + str(attachment)

        student = Student(student_id, first_name, last_name, age, address)
        roster.append(student)

        new_flag = input("Do you want to add another student(Y/N): ")
        if new_flag.lower() in ["y", "yes"]:
            flag = True
        elif new_flag.lower() in ["n", "no"]:
            flag = False
        else:
            print("You have entered an invalid key")
        attachment += 1

    return roster


students = register()


def print_student():
    print("----------------------------------")
    print("List of students registered so far")
    print("----------------------------------")

    for student in students:
        print(student.student_id + ": " + student.first_name + " " + student.last_name)
    print("----------------------------------")


def get_student(student_id):
    for student in students:
        if student.student_id == student_id:
            print(student.student_id + ": " + student.first_name + " " + student.last_name)
        else:
            print("Student not found")


print_student()


#get_student("Fan101")