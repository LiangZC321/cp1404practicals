from prac_07.guitar import Guitar


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

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

main()