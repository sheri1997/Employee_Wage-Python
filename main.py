import random
'''Using Random Function to generate a Random Number
   initialising the present value as 1
   and comparing it with the randomly generated value'''
present_employee=1
a=random.randint(0,1)
if(a==1):
    print("Employee is Present")
else:
    print("Employee is Absent")