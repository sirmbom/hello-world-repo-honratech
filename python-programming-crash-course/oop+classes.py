<<<<<<< HEAD
class Student:
    def __init__(self, name, age, matricule, gpa, gender):
        self.name = name
        self.age = age
=======
# CREATING A CLASS
# ThisRIghtHereIsCalled Pascal casing

class Student:
    # A constructor is needed for the class
    def __init__(self, name, matricule, gpa, gender):  # 'self' is a default empty object
        # Attributes
        self.name = name
>>>>>>> 5770839e568ff6a08c058470e92f85d79d80f3db
        self.matricule = matricule
        self.gpa = gpa
        self.gender = gender

<<<<<<< HEAD
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
    
=======
    # Behaviours/Methods
    def register(self):
        return f"{self.name} is having matricule {self.matricule}"
    def take_lesson(self):
        return f"{self.name} with matricule {self.matricule} registered Geology"
    def drop_lesson(self):
        return f"{self.name} with matricule {self.gpa} dropped Geology"

first_student = Student("Allen", "UBa23PB162", 1.99, "Him")
second_student = Student("Nita", "UBa23PB025", 2.0, "Male")

print(f"First Student:\n{first_student.name}, {first_student.matricule}, {first_student.gpa}, {first_student.gender}")

print(f"First Student {second_student.name} is Taking Lesson '{second_student.drop_lesson()}'")
>>>>>>> 5770839e568ff6a08c058470e92f85d79d80f3db
