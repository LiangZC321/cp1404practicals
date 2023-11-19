min_score = 0
max_score = 100
excellent_score = 90
passable_score = 50

def main():
    import random

    score = random.randint(0, 100)
    result = evaluate_score(score)
    print(result)
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)


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


