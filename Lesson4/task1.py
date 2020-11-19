# Task 1 Payroll
import sys
hour, salar_hour, bonus = map(float, sys.argv[1:])
print('Employee salary: {:.2f}'.format(hour * salar_hour + bonus))
