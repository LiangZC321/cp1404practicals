minimum_length = 5
def main():

    password = get_password()

    print("*" * len(password))


def get_password():
    password = input("Enter the password: ")
    while len(password) < minimum_length:
        print("invalid length")
        password = input("Enter the password: ")
    return password


main()