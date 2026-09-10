class Student:
    def __init__(self, name, age, matricule, gpa, gender):
        self.name = name
        self.age = age
        self.matricule = matricule
        self.gpa = gpa
        self.gender = gender

    def register(self):
        return f"{self.name} is having matricule {self.matricule}"
    def take_lesson(self):
         return f"{self.name} with matricule {self.matricule} registered Geology"
    def take_lesson(self):
             return f"{self.name} with matricule {self.matricule} dropped Geology"

first_student = Student("Allen", "UBa23PB162", 1.99, "Him")
second_student = Student("Nita", "UBa23PB025", 2.00, "Male")

Print(f"First Studdent:\n{first_student.name}, {first-student.matricule}, {first_student.gpa}, {first_student.gender}")

print(f"First Student:{second_student.name}, is taking Lessons {second_student.drop_lesson()}")
    