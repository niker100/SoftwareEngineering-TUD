#  1. Write a program that prompts for two numbers, finds the remainder of the division of the first by the
# second, and outputs the result.
def e1():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    return a % b

# 2. Write a program that inputs three numbers, adds them, and outputs the result. Use as few variables as
# possible.
def e2():
    a = 0
    for i in range(1, 4):
        a = a + int(input(f'Enter the {i} number: '))
    return a

def e2_listComprehension():
    return sum([int(input(f'Enter the {i} number: ')) for i in range(1, 4)])

# 3. Enter a number. Print 1 if the number is even, and 0 if the number is odd.
def e3():
    return int(input('Enter a number: ')) % 2

# 4. Input two numbers. Print first the smaller one, then the larger one.
def e4():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    if a <= b:
        return a, b
    return b, a

#  5. Determine if the following conditions are true or false:
#  a. not ((6 < 4) and (4 > 8))
#  b. (a <= a + 1) or (12 - 3 > 0)
#  c. ((2 <= 2) and (3 >= 3)) or (15 > 25)
# in console

#  6. Input three numbers. Select and print the largest of them.
def e6():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    c = int(input('Enter the third number: '))
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

# 7. Write a program that prompts for the time of day and, based on the input, wishes good morning, good
# afternoon, good evening, or good night.
def e7():
    time = int(input('Enter the time of day: ').split(':')[0]) % 24
    if 0 <= time < 12:
        return 'Good morning'
    elif 12 <= time < 18:
        return 'Good afternoon'
    elif 18 <= time < 22:
        return 'Good evening'
    return 'Good night'