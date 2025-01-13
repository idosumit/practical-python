import csv


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
