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


color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(color_name, "is", COLOR_CODES[color_name])
    except KeyError:
        print("Invalid color name")

    color_name = input("Enter color name: ").lower()