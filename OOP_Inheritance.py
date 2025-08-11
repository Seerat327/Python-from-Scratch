#Car Inheritance Example
class Vehicle:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def info(self):
        print(f"The car model is {self.model} and the brand of the car is {self.brand}")
class car(Vehicle):
    def __init__(self,model,brand,seats):
        self.seats=seats
        super().__init__(model,brand)
    def details(self):
        print(f"The no. of seats in the car are {self.seats}")
car1=car('Verna','Hyundai','5')
car1.info()
car1.details()
        
#Cat and Dog Inheritance 
class Animal:
    def __init__(self):
        pass
    def speak(self):
        print('Animal makes a sound')
class dog(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print('Dog barks')
class cat(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Cat meows")
animal=Animal()
animal.speak()
Dog=dog()
Dog.speak()

#School Management System
class StudentMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Teacher(StudentMember):
    def __init__(self,name,age,subject):
        self.subject=subject
        super().__init__(name,age)
    def show_details(self):
        print(f" Name:{self.name} , Age:{self.age},Subject: {self.subject}")
class Student(StudentMember):
    def __init__(self,name,age,grade):
        self.grade=grade
        super().__init__(name,age)
    def show_details(self):
        print(f" Name:{self.name} , Age:{self.age} ,Grade: {self.grade}")

student1=Student('Harsh','12','A')
student1.show_details()
Teacher1=Teacher('Amrita','32','Math')
Teacher1.show_details()



    
    
