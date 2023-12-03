import csv
from collections import defaultdict

def read_csv(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.DictReader(in_file)
        data = list(reader)
    return data

def process_champions(data):
    champion_wins = defaultdict(int)
    for row in data:
        champion = row["Champion"]
        champion_wins[champion] += 1
    return champion_wins

def process_countries(data):
    countries_set = set()
    for row in data:
        country = row["Country"]
        countries_set.add(country)
    return countries_set

def display_champions(champion_wins):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")

def display_countries(countries_set):
    sorted_countries = sorted(countries_set)
    countries_string = ", ".join(sorted_countries)
    print("\nThese countries have won Wimbledon:")
    print(countries_string)

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    champion_wins = process_champions(data)
    display_champions(champion_wins)

    countries_set = process_countries(data)
    display_countries(countries_set)


main()