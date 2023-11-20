name_file = open("name.txt", 'w')
user_name = input("Enter your name: ")
print(user_name, file=name_file)
name_file.close()

name_file = open("name.txt", "r")
user_name = name_file.read()
print(f"Your name is {user_name}")


number_file = open("numbers.txt", "r")

num1 = int(number_file.readline())
num2 = int(number_file.readline())
sum_numbers = num1 + num2
print(f"Sum of the first two numbers: {sum_numbers}")
number_file.close()

number_file = open("numbers.txt", "r")
all_numbers = [int(line) for line in number_file.readlines()]
total_of_all = sum(all_numbers)
print(f"Total for all numbers: {total_of_all}")

