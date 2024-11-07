"""
File: lucky_ticket.py
Author: Nick Schubert
Date: 07.11.2024
@TU Dresden


Task: Count how many six-digit numbers have equal sums of the first three and the last three digits.
This is also known as the "lucky ticket" problem, but we are only interested in real 6-digit numbers (no leading zeros).
"""

import time

# Whole range, sum using list comprehension
# this is the most straightforward solution, but also the slowest
# note that this was the solution GPT-4o came up with
def f1_stringConversion():
    count = 0
    for i in range(100000, 1000000):
        if sum(int(digit) for digit in str(i)[:3]) == sum(int(digit) for digit in str(i)[3:]):
            count += 1
    return count

# f1 without list comprehension and using a simple loop
# faster than f1 because it avoids the overhead of creating a list and iterating over it
def f1_simpleLoop():
    count = 0
    for i in range(100000, 1000000):
        upper_sum = 0
        lower_sum = 0
        for j in range(3):
            upper_sum += int(str(i)[j])
            lower_sum += int(str(i)[j + 3])
        if upper_sum == lower_sum:
            count += 1
    return count

# Whole range, sum using map
# this is faster than f1_simple because it avoids the loop and uses the built-in and highly optimized map function
def f2_map():
    count = 0
    for i in range(100000, 1000000):
        if sum(map(int, str(i // 1000))) == sum(map(int, str(i % 1000))):
            count += 1
    return count

# Decomposed range, sum using map
# This is faster than f2 because it avoids the repeated calculation of the upper sum for each lower part, which is the same for all lower parts
def f3_decomposition():
    count = 0
    for upper in range(100, 1000):
        upper_sum = sum(map(int, str(upper)))
        for lower in range(0, 1000):
            if upper_sum == sum(map(int, str(lower))):
                count += 1
    return count


# Decomposed range, sum using integer division and modulo
# This is faster than f3 because it avoids the overhead of converting integers to strings and back
def f4_decompositionModulo():
    count = 0
    for upper in range(100, 1000):
        upper_sum = upper // 100 + (upper // 10) % 10 + upper % 10
        for lower in range(0, 1000):
            if (upper_sum ==
                lower // 100 + (lower // 10) % 10 + lower % 10):
                count += 1
    return count

# Nested loops over each digit
# in comparison actually pretty efficient, mainly because it avoids converting integers to strings and division operations
# uses only integer addition and comparison which are very fast in hardware
# note that for 8 digits this ran in 2.88 seconds and for 10 digits in 339.65 seconds on my machine
# this has a time complexity of O(10^n) where n is the number of digits
def f5_singleDigits():
    count = 0
    for d1 in range(1, 10):   # First digit (cannot be zero for six-digit numbers)
        for d2 in range(10):
            for d3 in range(10):
                sum_first = d1 + d2 + d3
                for d4 in range(10):
                    for d5 in range(10):
                        for d6 in range(10):
                            sum_second = d4 + d5 + d6
                            if sum_first == sum_second:
                                count += 1
    return count

# Precompute possible sums for valid first three digits (100 to 999) and last three digits (000 to 999)
# then multiply the counts for each sum to get the total count of lucky tickets
# This is the most efficient solution, as it avoids nested loops and string conversions
# instead of checking 900000 numbers, we only need to calculate the sums for 1900 numbers and multiply the counts for matching sums
# because we're dividing the the number into two parts, the time complexity is now O(10^(n/2)) or O(sqrt(10^n)) instead of O(10^n) which is much faster
def f6_divideAndConquer():
    # Dictionary to store counts of each sum (0-27) for combinations of 3 digits
    sum_counts_upper = {k: 0 for k in range(28)}
    sum_counts_lower = {k: 0 for k in range(28)}
    
    # Calculate possible sums for the first three digits (100-999, so d1 starts from 1)
    for d1 in range(1, 10):  # d1 can't be 0 for valid 6-digit numbers
        for d2 in range(10):
            for d3 in range(10):
                s = d1 + d2 + d3
                sum_counts_upper[s] += 1

    # Calculate possible sums for the last three digits (000-999, so all digits range from 0-9)
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                s = d1 + d2 + d3
                sum_counts_lower[s] += 1
    
    # Now count lucky tickets by multiplying the combinations for matching sums
    count = sum(sum_counts_upper[s] * sum_counts_lower[s] for s in range(28))
    return count


# comparison:
# in f5 we have 900*2 additions for sum_first, 900,000*2 additions for sum_second, 900,000 comparisons and 900,000 increments for count
# that is 3,601,800 operations
#
# in f6 we have 900*2 additions for sum_first, 1000*2 additions for sum_second, 900+1000 increments for sum_counts_upper and sum_counts_lower
# and 28 additions and 28 multiplications for the final count
# that is 5,756 operations
# an improvement by a factor of >600

# algorithm f6 generalized for any number of digits, but using string conversion for easier implementation
# takes about 0.1 seconds for 10 digits compared to 339.65 seconds for f5_10digits
def f6_generalized(digit_count=10):
    # Half the number of digits
    half_digit_count = digit_count // 2

    print(f"Calculating lucky tickets for {digit_count} digits...")
    
    # Maximum sum for each half (each digit can range from 0 to 9, so max sum for half is 9 * half_digit_count)
    max_sum = 9 * half_digit_count
    
    # Create dictionaries to store counts of each sum for the two halves
    sum_counts_upper = {k: 0 for k in range(max_sum + 1)}
    sum_counts_lower = {k: 0 for k in range(max_sum + 1)}
    
    # Calculate possible sums for the first half (digits from 1 to 9 for the first digit, 0-9 for others)
    for digits_upper in range(10**(half_digit_count - 1), 10**half_digit_count):  # First half
        digit_sum = sum(int(digit) for digit in str(digits_upper))
        sum_counts_upper[digit_sum] += 1
    
    # Calculate possible sums for the second half (digits 0-9 for all positions)
    for digits_lower in range(0, 10**half_digit_count):  # Second half
        digit_sum = sum(int(digit) for digit in str(digits_lower))
        sum_counts_lower[digit_sum] += 1
    
    # Now count lucky tickets by multiplying the combinations for matching sums
    count = sum(sum_counts_upper[s] * sum_counts_lower[s] for s in range(max_sum + 1))
    return count

# takes 5 to 10 minutes for 10 digits
def f5_10digits():
    count = 0
    for d1 in range(1, 10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in range(10):
                    for d5 in range(10):
                        sum_first = d1 + d2 + d3 + d4 + d5
                        for d6 in range(10):
                            for d7 in range(10):
                                for d8 in range(10):
                                    for d9 in range(10):
                                        for d10 in range(10):                                            
                                            sum_second = d6 + d7 + d8 + d9 + d10
                                            if sum_first == sum_second:
                                                count += 1
    return count

# Measure and print the execution time for each function
functions = [f1_stringConversion, f1_simpleLoop, f2_map, f3_decomposition, f4_decompositionModulo, f5_singleDigits, f6_divideAndConquer, f6_generalized, f5_10digits]
for func in functions:
    start_time = time.time()
    count = func()
    end_time = time.time()
    print(f"Function {func.__name__:<25}: count = {count}, Execution time = {end_time - start_time:.6f} seconds")

# Outputs:
# Function f1_stringConversion      : count = 50412, Execution time = 0.678644 seconds
# Function f1_simpleLoop            : count = 50412, Execution time = 0.532004 seconds
# Function f2_map                   : count = 50412, Execution time = 0.402004 seconds
# Function f3_decomposition         : count = 50412, Execution time = 0.191910 seconds
# Function f4_decompositionModulo   : count = 50412, Execution time = 0.041502 seconds
# Function f5_singleDigits          : count = 50412, Execution time = 0.026000 seconds
# Function f6_divideAndConquer      : count = 50412, Execution time = 0.000000 seconds
# Function f5_8digits               : count = 4379055, Execution time = 2.879499 seconds
# Function f6_8digits               : count = 4379055, Execution time = 0.009501 seconds
# Function f5_10digits              : count = 392406145, Execution time = 327.078651 seconds
# Function f6_10digits              : count = 392406145, Execution time = 0.091571 seconds
