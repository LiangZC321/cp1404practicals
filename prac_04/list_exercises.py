numbers = []

for i in range(5):
    num = float(input("Number: "))
    numbers.append(num)

print("\nThe first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))