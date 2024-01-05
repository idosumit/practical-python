# mortgage.py

# Exercise 1.9 and 1.10 answers

"""
TO ME IN THE FUTURE: Resulting principal here is different than the website sample towards the end.
I tried debugging with GPT-4 as well. The principal still stays different than the website's
principal towards the end. Basically dunno why, but I believe this may be something to do with
the hideous formatting of the code. I'll leave as it is for now. Maybe I'll know a better way
to format my code when I revisit this again during the revision stage.
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0 and months < extra_payment_start_month:
    principal = (principal * (1+rate/12) - payment)
    total_paid = (total_paid + payment)
    months += 1
    print(f"{months} {total_paid:.2f} {principal:.2f}")

while principal > 0 and months <= extra_payment_end_month:
    principal = (principal * (1+rate/12) - payment - 1000)
    total_paid = (total_paid + payment + 1000)
    months += 1
    print(f"{months} {total_paid:.2f} {principal:.2f}")

while principal > 0 and months > extra_payment_end_month:
    principal = (principal * (1+rate/12) - payment)
    total_paid = (total_paid + payment)
    months += 1
    print(f"{months} {total_paid:.2f} {principal:.2f}")

print(f"Total paid {total_paid:.2f} \nMonths {months}")