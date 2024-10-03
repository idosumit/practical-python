principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
time = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0: 
    while extra_payment_start_month < time <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        time += 1
        print(f'{time} {total_paid:.2f} {principal:.2f}')


    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    time += 1

    print(f'{time} {total_paid:.2f} {principal:.2f}')

print(f'Total paid {total_paid:.2f}')

print(f'Months {time}')
