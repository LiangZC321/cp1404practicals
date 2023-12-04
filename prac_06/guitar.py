#10:56 started
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50


def get_user_guitars():
    guitars = []
    guitar_number = 1

    name = input("Name: ")
    while name != "":

        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.")
        guitar_number += 1
        name = input("Name: ")

    return guitars


def display_user_guitars(guitars):
    print("\nThese are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        vintage_status = "(vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar}, worth ${guitar.cost:.2f} {vintage_status}")



print("My guitars!")
user_guitars = get_user_guitars()
display_user_guitars(user_guitars)