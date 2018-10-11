import json
import sys

fname = sys.argv[1]
data = json.load(open(fname, 'r'))
print("items:", len(data))

print("length item", len(data[0]))
print("keys per item", data[0][0].keys())

dates = set()
for snapshot in data:
    for item in snapshot:
        dates.add(item['dateObserved']['value'])

ldates = sorted(list(dates))
print(min(ldates), max(ldates))