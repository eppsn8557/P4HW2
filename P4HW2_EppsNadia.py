 # CTI-110

   # P4HW2 - Salary Calculator

   # Nadia Epps

   # 15 November 2023

   #
num_employee = 0
total_ovr_time_pay = 0
total_reg_pay = 0
total_gross_pay = 0
pay_rate = 0
ovr_time = 0
ovr_time_pay = 0
reg_pay = 0
gross_pay = 0


valid = "N"
while valid == "N":
    employee_name = input(f"Enter employee's name or 'Done' to terminate: ")

    if employee_name.lower () == "done":
        valid = "Y"
    else:
        num_employee = num_employee + 1
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

        if hours_worked > 40:
            ovr_time = hours_worked - 40
            ovr_time_pay = ovr_time * (pay_rate * 1.5)
            total_ovr_time_pay = total_ovr_time_pay + ovr_time_pay
            hours_worked = hours_worked - ovr_time
        

        reg_pay = hours_worked * pay_rate
        total_reg_pay = total_reg_pay + reg_pay
        gross_pay = total_ovr_time_pay + reg_pay
        hours_worked = hours_worked + ovr_time
        total_ovr_time_pay + ovr_time_pay
        total_reg_pay + reg_pay
        total_gross_pay += gross_pay
        

        print()
        print('Employee name:', employee_name)
        print()
        print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
        print('-------------------------------------------------------------------------------')
        print(f"{hours_worked:<15.2f} {pay_rate:<10.2f} {ovr_time:<10.1f}   {ovr_time_pay:<10.2f}  {reg_pay:<10.2f} {gross_pay:<8.2f} ")
        print()
print(f'Total number of employees entered: {num_employee} ' )
print(f'Total amount paid for overtime:   ${total_ovr_time_pay:.2f}')
print(f'Total amount paid for regular hours:   ${total_reg_pay:.2f}')                         
print(f'Total amount paid in gross:   ${total_gross_pay:.2f}')
