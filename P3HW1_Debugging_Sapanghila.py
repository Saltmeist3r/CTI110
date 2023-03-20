print('#CTI-110\n#P3HW1- Student Grade List\n#Sapanghila,Ira Chriel\n#March 21, 2023')
print('')
print('')
print('')
m1 = float(input('Enter grade for Module 1: '))
m2 = float(input('Enter grade for Module 2: '))
m3 = float(input('Enter grade for Module 3: '))
m4 = float(input('Enter grade for Module 4: '))
m5 = float(input('Enter grade for Module 5: '))
m6 = float(input('Enter grade for Module 6: '))

lowest_grade = min(m1, m2, m3, m4, m5, m6)
highest_grade =max(m1, m2, m3, m4, m5, m6)
sum_grade = float(m1 + m2 + m3 + m4 + m5 + m6)
average = float(m1 + m2 + m3 + m4 + m5 + m6) /6

print('')
print('')
print('------------Results-----------')
print (f'Lowest Grade:         {lowest_grade}')
print (f'Highest Grade:        {highest_grade}')
print (f'Sum of Grades:        {sum_grade}')
print (f'Average:              {average:.2f}')
print('------------------------------')
def calcAverage(sum_grade):
   average = float(sum_grade/6)
   return average

def determineGrade(average):
    if average >= 90:
        print('Your grade is: A ')
    elif average >= 80:
        print('Your grade is: B ')
    elif average >= 70:
        print('Your grade is: C ')
    elif average >= 60:
        print('Your grade is: D: ')
    else:
        print('Your grade is: E.')
average = calcAverage(sum_grade)
determineGrade(average)
input('press ENTER to exit')
