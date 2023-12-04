from prac_06.guitar import Guitar
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