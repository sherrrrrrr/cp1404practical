def main():
    password = get_password()
    print_password_asterisks(password)

def get_password():
    password = input("Enter password: ")
    return password

def print_password_asterisks(password):
    print('*' * len(password))




if __name__ == "__main__":
    main()
