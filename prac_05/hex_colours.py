COLOR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chocolate": "#d2691e",
    "darkorchid": "#9932cc",
    "firebrick": "#b22222",
    "gainsboro": "#dcdcdc",
    "indianred": "#cd5c5c"
}


print(COLOR_CODES)

for color_name, color_code in COLOR_CODES.items():
    print("{:<4} {}".format(color_name, "is " + color_code))

color_name = input("Enter short state: ").lower()
while color_name != "":
    try:
        print(color_name, "is", COLOR_CODES[color_code])
    except KeyError:
        print("Invalid color name")

    color_name = input("Enter short state: ").lower()