def get_name(email):
    name = email.split('@')[0]
    name = name.title()

    return name

user_data = {}
email = input("Email: ")
while email != "":
    name = get_name(email)
    confirm_name = input(f"Is your name {name}? (Y/n) ").lower()
    if confirm_name not in ('', 'y'):
        name = input("Name: ")
    user_data[email] = name
    email = input("Email: ")

print("\ndata:")
for email, name in user_data.items():
    print(f"{name} ({email})")