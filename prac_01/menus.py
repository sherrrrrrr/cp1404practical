name = input("Enter name: ")

choice = ""
while choice.upper() != 'Q':
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    elif choice != 'Q':
        print("Invalid choice")

print("Finished.")