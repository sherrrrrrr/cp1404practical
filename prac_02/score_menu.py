from score import get_result


def main():
    score = get_valid_score()

    choice = ''
    while choice != 'Q':
        display_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
        else:
            print("Invalid input, please try again.")


def display_menu():
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score, please try again.")
            else:
                return score
        except ValueError:
            print("Invalid input, please try again.")


def print_result(score):
    result = get_result(score)
    print("Result:", result)


def show_stars(score):
    print("Stars: " + "*" * int(score / 10))

if __name__ == '__main__':
    main()
