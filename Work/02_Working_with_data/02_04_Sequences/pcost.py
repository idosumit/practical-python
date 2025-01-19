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
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        total_cost = 0

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
