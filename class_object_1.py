class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks 
        
    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
     
    def is_pass(self):
        
        if self.marks>=40:
            return "pass"
        else:
            return "fail"
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"
        
student1 = student("Alice", 101, 85)
student2 = student("Bob", 102, 35)
student3 = student("Charlie", 103, 92)

students = [student1, student2, student3]
for student in students:
    student.display_details()
    print("Result:", student.is_pass())
    print("Grade:", student.grade())
    print("-" * 30)
    