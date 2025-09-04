class Student:
    def __init__(self,name,roll_no,age,grades):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.grades=grades

    def info(self):
        print(f'Student Name : {self.name}')
        print(f'Student roll_no : {self.roll_no}')
        print(f'Student age:{self.age}')
        print(f'Student grades : {self.grades}')

    def update_grades(self, subject, marks):
        self.grades[subject] = marks
        print(f"Updated {self.name}'s grade in {subject} to {marks}")

class StudentManager:
    def __init__(self):
        self.students={}
    def add_student(self,name,roll_no,age,grades):
        if roll_no in self.students:
            print(f'Student with {roll_no} already exists')
        else:
            student=Student(name,roll_no,age,grades)
            self.students[roll_no]=student
            print(f'Student with roll no {roll_no} added succesfully')
    def view_student(self):
        if not self.students:
            print('No student found in record')
        else:
            for student in self.students.values():
                student.info()
                print()
    def search_student(self,roll_no):
        student=self.students.get(roll_no)
        if student:
            student.info()
        else:
            print('Student not found')
    def update_student_grade(self,roll_no,subject,marks):
        student=self.students.get(roll_no)
        if student:
            student.update_grades(subject,marks)
        else:
            print('Student not found')

manager=StudentManager()
manager.add_student('Ajay',12,14,{'English':98 , 'Science':84})
manager.search_student(12)
manager.update_student_grade(12,'English',89)
manager.view_student()
    
    



        
