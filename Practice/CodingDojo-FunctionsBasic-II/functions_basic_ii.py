"""
Functions basic II

1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
"""
# 1. Countdown
def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
    
# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

# 3. First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

# 4. Values Greater than Second
def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

# 5. This Length, That Value
def length_and_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list

print(countdown(5))
print(print_and_return([1,2]))
print(first_plus_length([1,2,3,4,5]))
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
print(length_and_value(4,7))
print(length_and_value(6,2))