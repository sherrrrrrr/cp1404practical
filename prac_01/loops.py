# Displaying all the odd numbers between 1 and 20 with a space between each one.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
num_stars = int(input("Number of stars: "))
for i in range(num_stars):
    print('*', end='')
print()

# d. print n lines of increasing stars. Using the same number as above,
# print lines of increasing stars, starting at 1 with no blank line.
for i in range(1, num_stars + 1):
    print('*' * i)