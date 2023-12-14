#CTI-110
#P4HW2- Salary Calculator
#Glover, Joshua
#22NOV2023

# ask user to enter name of employee
employee_name = input("Enter Employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
# calculate over time
over_time = (hours_worked - 40)
#calculate overtime pay
over_time_pay = ((hours_worked - 40) * (pay_rate * 1.5))
#calculate reghour pay
reghour_pay = ((hours_worked - over_time) * pay_rate) 
print('-------------------------------')
print("Employee name:" , '   ',   employee_name)
print()
print("hours Worked   Pay Rate   OverTime   Overtime Pay   RegHour Pay")
print("----------------------------------------------------------------")
print(hours_worked,    pay_rate,  over_time, over_time_pay, reghour_pay)

employee_name = []
employees = 0
while employees < 5:
    name = input(" Enter the employee's name or Done to terminate: ")
    employee_name.name.apppend(name)
    employees += 1
    print(employee_name)
