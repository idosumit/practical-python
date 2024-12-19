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
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        every_row = []
    
        total_cost = 0

        for row in rows:
            every_row.append(row)

        for row in every_row:
            try:
                row_cost = float(row[-1]) * float(row[-2])
            except ValueError:
                print('empty strings found in the row array:', row)
            total_cost += row_cost
    
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost:", cost)
