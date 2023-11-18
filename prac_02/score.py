min_score = 0
max_score = 100
import random

def generate_random_score(min_score, max_score):
    return random.randint(min_score, max_score)
random_score = generate_random_score(min_score, max_score)


def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"

