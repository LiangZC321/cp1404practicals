import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_QUICK_PICKS = 6

def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_QUICK_PICKS))

def main():
    # user part
    num_quick_picks = int(input("How many quick picks? "))
    for i in range(1, num_quick_picks + 1):
        quick_pick = generate_quick_pick()
        for number in quick_pick:
            print(f"{number:2}", end=" ")
        print()

main()
