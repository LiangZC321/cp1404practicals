MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
  print(MENU)
  choice = input(">>> ").upper()
  while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"fahrenheit: {fahrenheit}")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"celsius: {celsius}")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
  print("Thank you.")



def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
main()