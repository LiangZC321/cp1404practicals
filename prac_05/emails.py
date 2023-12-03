def get_name(email):
    name_parts = email.split('@')[0].split('.')
    name = ' '.join(part.title() for part in name_parts)


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