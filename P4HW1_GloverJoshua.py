while True:
    employee_name = input("Enter Employee's name (or type 'done' to quit): ")
    
    if employee_name.lower() == 'done':
        break  # exit the loop if the user enters 'exit'

    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # calculate over time
    over_time = max(0, hours_worked - 40)

    # calculate overtime pay
    over_time_pay = over_time * pay_rate * 1.5

    # calculate regular hour pay
    reghour_pay = (hours_worked - over_time) * pay_rate

    print('-------------------------------')
    print("Employee name:", employee_name)
    print()
    print("Hours Worked   Pay Rate   OverTime   Overtime Pay   RegHour Pay")
    print("----------------------------------------------------------------")
    print(f"{hours_worked}             {pay_rate}        {over_time}              {over_time_pay}          {reghour_pay}")
    print('-------------------------------')
    
    
