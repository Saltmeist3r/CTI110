print('#CTI-110\n#P4HW2 - Salary Calculator\n#Sapanghila,Ira Chriel\n#April 18, 2023')
print('')
employee_count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

employee_name = input("Enter employee's name: ")
hours_worked = float(input(f"How many hours did {employee_name} work? "))
pay_rate = float(input(f"What is {employee_name}'s pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    overtime_hours = 0
    overtime_pay = 0

regular_hours = hours_worked - overtime_hours
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

total_overtime_pay += overtime_pay
total_regular_pay += regular_pay
total_gross_pay += gross_pay

employee_count += 1

print('----------------------------------')
print(f"Employee name: {employee_name}")
print('')
print('Hours worked    Pay rate    OverTime    Overtime Pay    RegHour Pay    Gross Pay')
print('--------------------------------------------------------------------------------')
print(f"{hours_worked:.1f}        {pay_rate:>8.2f}    {overtime_hours:>8.1f}{overtime_pay:>12.2f}            ${regular_pay:.2f}        ${gross_pay:>.2f}")
 
while True:
    employee_name = input('Enter employee\'s name or "Done" to terminate program: ')
    
    if employee_name.lower() == 'done':
        print(f'Total number of employees entered: {employee_count}')
        print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
        print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
        print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
        break
        
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate: "))
    
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        overtime_hours = 0
        overtime_pay = 0

    regular_hours = hours_worked - overtime_hours
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    
    employee_count += 1

    print('----------------------------------')
    print(f"Employee name: {employee_name}")
    print('')
    print('Hours worked    Pay rate    OverTime    Overtime Pay    RegHour Pay    Gross Pay')
    print('--------------------------------------------------------------------------------')
    print(f"{hours_worked:.1f}        {pay_rate:>8.2f}    {overtime_hours:>8.1f}  {overtime_pay:>12.2f}          ${regular_pay:.2f}        ${gross_pay:>.2f}")
