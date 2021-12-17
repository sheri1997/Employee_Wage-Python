import random

'''Using Random Function to generate a Random Number
   initialising the present value as 1
   and comparing it with the randomly generated value'''
present_employee = 1
wage_per_hour = 20
hours = 0
wage = 0
a = random.randint(0, 1)
if (a == 1):
    hours = 8
else:
    hours = 0
wage = hours*wage_per_hour
print("Wage of the Employee = ", wage)
