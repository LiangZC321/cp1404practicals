import csv
from collections import defaultdict

filename = "wimbledon.csv"

champion_wins = defaultdict(int)
countries_set = set()

with open(filename, "r", encoding="utf-8-sig") as in_file:
    reader = csv.DictReader(in_file)

    for row in reader:
        champion = row["Champion"]
        country = row["Country"]
        champion_wins[champion] += 1
        countries_set.add(country)

print("Wimbledon Champions:")

