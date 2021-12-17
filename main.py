import random

'''Using Random Function to generate a Random Number
   initialising the values of different variables
   and comparing it with the randomly generated value'''
part_time_employee = 1
full_time_employee = 2
wage_per_hour = 20
hours = 0
wage = 0
monthly_wage = 0
working_days = 2
total_working_days = 0
hours_in_a_month = 100
total_employee_hours = 0
'''loop will check if the total employee hours is less 
    or equal to the total working hours in a month and 
    at the same time total working days is less than 
    the working days in a month.'''
while total_employee_hours <= hours_in_a_month and total_working_days<working_days:
    total_working_days = total_working_days+1
    a = random.randint(0, 1)
    if a == 1:
        hours = 8
    else:
        hours = 16
    total_employee_hours = total_employee_hours + hours
total_wage = total_employee_hours * wage_per_hour
print("Total Wage of the Employee is :",total_wage)
