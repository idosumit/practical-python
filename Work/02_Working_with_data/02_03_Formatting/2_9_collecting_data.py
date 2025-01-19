# start of the file

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = {"name": row[0], "shares": int(
                row[1]), "price": float(row[2])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices_dict = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) < 1:
                pass
            else:
                prices_dict[row[0]] = float(row[1])
    return prices_dict


# the person's portfolio
portfolio = read_portfolio("Work/Data/portfolio.csv")

# market prices
prices = read_prices("Work/Data/prices.csv")

# calculating the prices the person paid to buy shares
# according to portfolio.csv
total_portfolio_cost = 0.0
for i in portfolio:
    total_portfolio_cost += i["shares"] * i["price"]

# caculating the actual current market value of those shares
# according to prices.csv
total_market_val = 0.0
for j in portfolio:
    total_market_val += j["shares"] * prices[j["name"]]

"""
# gain / loss based on this info
print(
    f'''Total Portfolio Cost: {total_portfolio_cost}
Total Market Valuation of the stocks the person holds: {total_market_val}
Gain/Loss: {total_portfolio_cost - total_market_val}
'''
)
"""


def make_report(portfolio, prices):
    report = []
    for i in portfolio:
        name = i["name"]
        shares = i["shares"]
        market_price = prices[i["name"]]
        paid_price = i["price"]
        change = paid_price * shares - market_price * shares
        row = (name, shares, market_price, change)
        report.append(row)
    return report

# One-shotted this niceeeeeeee
