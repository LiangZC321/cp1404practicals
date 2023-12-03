def get_name(email):
    name = email.split('@')[0]
    name = name.title()

    return name