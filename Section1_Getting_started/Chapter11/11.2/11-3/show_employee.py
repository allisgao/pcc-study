# coding=utf-8
from employee import Employee

employee = Employee('albert', 'einstan', 300000)
salaries = employee.give_rise()
print(salaries)

salaries2 = employee.give_rise(10000)
print(salaries2)