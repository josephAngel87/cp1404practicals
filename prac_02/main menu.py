"""main menu"""
import random
def main()
    menu()

def menu()
    name = input("What is your name: ")
    choice = input("(N)ame   (G)enerate new   (Q)uit   :")
    while choice != "Q":
        if choice == "N":
            print("Your name is ", name)
        elif choice == "G":
            name = random.
            print(, name)
        else:
            print("Invalid Message!")
        choice = input("(N)ame   (G)enerate new   (Q)uit   :")