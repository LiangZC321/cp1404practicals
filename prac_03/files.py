name_file = open("name.txt", 'w')
user_name = input("Enter your name: ")
print(user_name, file=name_file)
name_file.close()

name_file = open("name.txt", "r")
user_name = name_file.read()
print(f"Your name is {user_name}")
name_file.close()