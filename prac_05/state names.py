"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
for abbreviation in CODE_TO_NAME:
    print(f"{abbreviation:3} is short for {CODE_TO_NAME[abbreviation]:3}")

state_code = input("Enter short state: ")
state_code = state_code.upper()
while state_code != "":
    state_code = state_code.upper()
    try:
        #state_code in CODE_TO_NAME
        print(state_code, "is", CODE_TO_NAME[state_code])
    except ValueError:
        print("Invalid short state")
    state_code = input("Enter short state: ")