# 1.27 Reading a data file

"""
inside the portfolio.csv file:

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

"""

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
    
        every_row = []
    
        for line in f:
            row = line.split(',')
            every_row.append(row)

        total_cost = 0
        for row in every_row:
            try:
                row_cost = float(row[-1]) * float(row[-2])
            except ValueError:
                print('empty strings found in the row array:', row)
            total_cost += row_cost
    
        print(f'Total cost {total_cost}')

