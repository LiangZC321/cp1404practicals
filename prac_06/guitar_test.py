from guitar import Guitar


gibson_l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
current_year = 2022
print(gibson_l5)
print(f"The guitar is {gibson_l5.get_age(current_year)} years old.")
print(f"Is the guitar vintage? {gibson_l5.is_vintage(current_year)}")