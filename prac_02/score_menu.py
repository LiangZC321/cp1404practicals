"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""
min_score = 0
max_score = 100
excellent_score = 90
passable_score = 50

def main():
    import random

    score = random.randint(0, 100)
    display_menu()
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "g":
            score = float(input("Enter score:(0-100):"))
        elif choice == "p":
            result = evaluate_score(score)
            print(result)
        elif choice == "s":
            print("*" * score)
        else:
            print("invalid choice")
        display_menu()
        choice = input("Enter your choice: ").lower()
    print("farewell")

def display_menu():
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def evaluate_score(score):
    if score < min_score or score > max_score:
        result = "Invalid score"
    else:
        if score >= excellent_score:
            result = "Excellent"
        elif score >= passable_score:
            result = "Passable"
        else:
            result = "Bad"
        return result

main()





