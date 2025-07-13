import csv
import pprint

with open("../data/data-text.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    pprint.pprint(next(reader))
    pprint.pprint(next(reader))
