# mortgage.py
#
# Exercise 1.7

"""
Enter this program and run it. You should get an answer of 966,279.6.

DONE.
"""

"""
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid
along with the number of months required.

When you run the new program, it should report a total payment of 929,965.62 over 342 months.
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    while months <= 12:
        principal = principal * (1+rate/12) - payment - 1000
        total_paid = round((total_paid + payment + 1000), 7)
        months += 1

    principal = principal * (1+rate/12) - payment
    total_paid = round((total_paid + payment), 7) #rounded to 7 digits to get what the question asked for

print('Total paid', total_paid, 'over', months, 'months.')