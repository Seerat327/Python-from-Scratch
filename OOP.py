class Student:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def info(self):
        print(f"{self.Name} is {self.Age} years old")

a = Student("Anaya", "20")
a.info()
#Finding area and perimeter of rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def info(self):
        print(f"{self.area()} is the area and {self.perimeter()} is the perimeter of the rectangle")

a = Rectangle(int(input("length: ")), int(input("breadth: ")))
a.info()

# #Circle with variable radius 
class Circle:
    def __init__(self,radius):
     self.radius=radius
    def Area(self):
      return self.radius*self.radius*3.14
    def circumference(self):
      return 2*3.14*self.radius
    def info(self):
      print(f"{self.Area()} is the area of circle and {self.circumference()}is the perimeter of the circle")
a=Circle(int(input('radius: ')))
a.info()

#Comparing two circles
class Circle:
    def __init__(self,radius):
     self.radius=radius
    def Area(self):
      return self.radius*self.radius*3.14
    def circumference(self):
      return 2*3.14*self.radius
    def info(self):
      print(f"{self.Area()} is the area of circle and {self.circumference()}is the perimeter of the circle")
    def comparison(self,other_circle):
       return self.Area()/other_circle.Area()
    
a=Circle(int(input('radius: ')))
b=Circle(int(input('radius: ')))
a.info()
b.info()

print(f"comparison(A/B)={a.comparison(b)}")

#Employee Salary Tracker
class Employee:
    def __init__(self,name,salary,department):
      self.name=name
      self.salary=salary
      self.department=department
    def get_details(self):
       print(f" The name of the employee is{self.name} he/she works in this {self.department} department for this {self.salary} salary")
    def updated_salary(self,updated_salary):
       self.salary=updated_salary 
    def updated_department(self,updated_department):
       self.department=updated_department
a=Employee('Ajay','20000/-','Fire')
a.updated_department('HR')
a.updated_salary('12000/-')
a.get_details()

#Employee Salary Tracker
class Employee:
    def __init__(self,name,salary,department):
      self.name=name
      self.salary=salary
      self.department=department
    def get_details(self):
       print(f" The name of the employee is{self.name} he/she works in this {self.department} department for this {self.salary} salary")
    def updated_salary(self,updated_salary):
       self.salary=updated_salary 
    def updated_department(self,updated_department):
       self.department=updated_department
employees=[]

total_employees=int(input('Total no. of employees are : ' ))
for i in range(0,total_employees):
   print('Enter the details of the employees')
   Name=input('Name of the employee : ')
   Salary= int(input('Salary of the employee : '))
   Department=input('Department of the employee: ')
   emp=Employee(Name,Salary,Department)
   employees.append(emp)
for emp in employees:
 emp.get_details()

#Pass/Fail Checker:
class Student:
    def __init__(self,Name,Marks):
       self.Name=Name
       self.Marks=Marks
    def checker(self):
        if self.Marks>=40:
            return('Pass')
        else:
            return('fail')
    def info(self):
        print(f"{self.Name} has {self.checker()}ed the class")

print('The details of the students :')
Name=input('Enter the name of the student: ')
Marks=int(input('Enter the marks of the student : '))
Students=Student(Name,Marks)
Students.info()

#Student Grades Manager
class Student:
    def __init__(self,Name,marks1,marks2):
        self.Name=Name
        self.marks1=marks1
        self.marks2=marks2
        
    def checker1(self):
        if self.marks1>=90:
            return('A')
        if self.marks1>=80:
            return('B')
        if self.marks1>=70:
            return('C')
        else:
            return('D')
    def checker2(self):
        if self.marks2>=90:
            return('A')
        if self.marks2>=80:
            return('B')
        if self.marks2>=70:
            return('C')
        else:
            return('D')
    def average(self):
        return (self.marks1+self.marks2)/2
    def overall_grade(self):
        if self.average()>=90:
            return('A')
        if self.average()>=80:
            return('B')
        if self.average()>=70:
            return('C')
        else:
            return('D')
    def info(self):
        print(f"{self.Name} has got {self.marks1} in maths and {self.marks2} in english with an average of {self.average()} with an average grade of {self.overall_grade()}")
print('the details of the student')
Name=input('The name of the student is : ')
marks1=int(input('The marks in maths are: '))
marks2=int(input('The marks in english are: '))
a=Student(Name,marks1,marks2)
a.info()

    



      


 




