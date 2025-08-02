#try and except in division 
try:
    a=int(input('Enter a numerator:' ))
    b=int(input('Enter a denominator:' ))
    result=a/b
    print(f"Result:{result}" )
except ValueError:
    print('Wrong input')
except ZeroDivisionError:
    print('Zero cannot be a denominator')
finally:
    print('Task completed')
