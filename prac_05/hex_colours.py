"""
CP1404/CP5632 Practical 5
Hex colour dictionary lookup
"""

COLOUR_TO_INDEX = {"lilac": "#c8a2c8", "limegreen": "#32cd32", "linen": "faf0e6", "littleboyblue": "#6ca0dc",
                   "macaroniandcheese": "#ffbd88"}
colour_selected = input("Which colour: ")
while colour_selected != "":
    colour_selected = colour_selected.lower()
    try:
        print(colour_selected, "is", COLOUR_TO_INDEX[colour_selected])
    except KeyError:
        print("Invalid Colour")
    colour_selected = input("Which colour: ")
