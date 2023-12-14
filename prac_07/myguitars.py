from prac_07.guitar import Guitar
import csv


def read_guitars(file_name):
    guitars = []
    with open(file_name, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def main():
    file_name = 'guitars.csv'
    guitars = read_guitars(file_name)

    while True:
        add_more = input("Would you like to add a new guitar? (Y/N): ").upper()
        if add_more == 'N':
            break
        new_guitar = get_new_guitar()
        guitars.append(new_guitar)
    sorted_guitars = sorted(guitars)

    print("These are my guitars:")
    for guitar in sorted_guitars:
        print(guitar)
    write_guitars(file_name, sorted_guitars)


def get_new_guitar():
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: $"))
    return Guitar(name, year, cost)

def write_guitars(file_name, guitars):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
main()
