# to check if a number is positive,negative or equal to zero 

num=int(input())
if num>0:
    print('num is a positive number')
elif num<0:
    print('number is a negative number')
else:
    print('number is equal to zero')

# to check if a number is odd or even 

num=int(input())
if num%2==0:
    print(' the given number is even')
else :
    print('the given number is odd')

#to find the greatest of two numbers

a=int(input())
b=int(input())
if a>b:
    print('a is greater than b')
else:
    print('b is greater than a')

# Grading System

Total_Marks=int(input())
if Total_Marks>=90:
    print('Grade-A')
elif Total_Marks>=80:
     print('Grade-B')
elif Total_Marks>=70:
    print('Grade-C')
else : 
    print('Grade-D')

# login system using and operator 

username=input('enter your username-  ')
password=input('enter your password-  ')
if username=='adminn'and password=='123':
    print('login successful')
else:
    print('Wrong credentials')

#Find the largest number among the three given numbers 

a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print('a is greatest number')
elif b>=a and b>=c:
    print('b is greatest number')
else:
    print('c is greatest number')
