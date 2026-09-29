from winreg import QueryValue

name = input("Enter your name: ")
choice = input("(H)ello   (G)oodbye   (Q)uit   :")
while choice != "Q":
    if choice == "H":
        print("Hello ",name)
    elif choice == "G":
        print("Goodbye ",name)
    else:
        print("Invalid Message!")
    choice = input("(H)ello"
                   "(G)oodbye"
                   "(Q)uit")
print("Finished")