import random

'''Using Random Function to generate a Random Number
   initialising the present value as 1
   and comparing it with the randomly generated value'''
# present_employee = 1
part_time_employee = 1
full_time_employee = 2
wage_per_hour = 20
hours = 0
wage = 0
monthly_wage = 0
for day in range(1,21):
    a = random.randint(0, 1)
    if a == 1:
        hours = 8
    else:
        hours = 16
    wage = hours*wage_per_hour
    monthly_wage = monthly_wage + wage
print("Monthly Wage of the Employee = ", monthly_wage)

