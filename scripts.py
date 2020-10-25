#!/usr/bin/env python
import sys
import re
import textwrap
from abc import ABC
from datetime import datetime
from string import ascii_lowercase as letters, ascii_letters
from collections import Counter, OrderedDict, defaultdict, namedtuple, deque
import calendar
import email.utils
from html.parser import HTMLParser as DefaultHTMLParser
import xml.etree.ElementTree as etree


def execute_say_hello_world_challenge():
    """ Problem 1: Introduction 1/7 """
    print("Hello, World!")


def python_if_else_challenge_implementation(number: int, success=None, failure=None):
    success = success or "Not Weird"
    failure = failure or "Weird"
    if 1 <= number <= 100:
        if number % 2 != 0:
            # if odd - Weird
            return failure
        elif number in range(2, 6):
            # if even in [2, 5]
            return success
        elif number in range(6, 21):
            # if even in [6, 20]
            return failure
        else:
            # if even and greater than 20
            return success

    return "Out of constraints"


def execute_python_if_else_challenge():
    """ Problem 1: Introduction 2/7 """
    try:
        # read input
        user_input = input("Please enter a number from 1 to 100: ")
        # clean the input and convert to int
        user_input = int(user_input.strip())
        algo_output = python_if_else_challenge_implementation(number=user_input)
        print(algo_output)
    except TypeError:
        print("Could not convert input to integer")


def execute_arithmetic_operators_challenge():
    """ Problem 1: Introduction 3/7 """
    try:
        # read inputs, clean up and convert into ints
        a = int(input("Enter an integer: ").strip())
        b = int(input("Enter another integer: ").strip())
        # perform operations
        print(a + b)
        print(a - b)
        print(a * b)
    except TypeError:
        print("Could not convert input to integer")


def execute_numbers_division_challenge():
    """ Problem 1: Introduction 4/7 """
    try:
        # read inputs, clean up and convert into ints
        a = int(input("Enter an integer: ").strip())
        b = int(input("Enter another integer: ").strip())
        # perform division
        if b != 0:
            print(a // b)
            print(a / b)
    except TypeError:
        print("Could not convert input to integer")


def execute_loops_challenge():
    """ Problem 1: Introduction 5/7 """
    try:
        n = int(input("Enter a number: ").strip())
        for i in range(n):
            print(i ** 2)
    except TypeError:
        print("Could not convert input to integer")


def is_leap(year: int) -> bool:
    """
    An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
    It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
    A leap year contains a leap day.

    In the Gregorian calendar, three conditions are used to identify leap years:
        The year can be evenly divided by 4, is a leap year, unless:
            The year can be evenly divided by 100, it is NOT a leap year, unless:
                The year is also evenly divisible by 400. Then it is a leap year.

    This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
    while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

    """
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


def execute_function_is_leap_challenge():
    """ Problem 1: Introduction 6/7 """
    try:
        year = int(input("Enter a year: ").strip())
        print(is_leap(year))
    except TypeError:
        print("Could not convert input to integer")


def execute_print_function_challenge():
    """ Problem 1: Introduction 7/7 """
    # Example: print(*values, sep=' ', end='\n', file=sys.stdout)
    # Example: print(value1, value2, value3, sep=' ', end='\n', file=sys.stdout)
    try:
        number = int(input("Enter a number: ").strip())
        print(*range(1, number + 1), sep='')
    except TypeError:
        print("Could not convert input to integer")


def execute_lists_comprehension_challenge():
    """ Problem 1: Data types 1/6 """
    x = int(input("x = "))
    y = int(input("y = "))
    z = int(input("z = "))
    n = int(input("Coordinates sum should not be equal to: "))
    print(
        [
            [xx, yy, zz]
            for xx in range(x + 1)
            for yy in range(y + 1)
            for zz in range(z + 1)
            if xx + yy + zz != n
        ]
    )


def execute_runner_up_score_challenge():
    """ Problem 1: Data types 2/6 """
    # _ = int(input("Enter total number of scores: "))  # useless
    # read scores
    scores = re.split(r'\s+', input("Enter scores (numbers are separated by space): "))
    # convert into ints
    scores = map(int, scores)
    sorted_unique_scores = sorted(list(set(scores)), reverse=True)
    if len(sorted_unique_scores) > 1:
        up_runner_score = sorted_unique_scores[1]
        print(up_runner_score)
    else:
        print("Not sufficient number of diverse scores")


def execute_nested_lists_challenge():
    """ Problem 1: Data types 3/6 """
    # process inputs
    students_records = list()
    for _ in range(int(input("Enter number of students you want to include: "))):
        name = input("Student name: ").strip()
        score = float(input("Student score: ").strip())
        students_records.append([name, score])
    # find the second lowest score
    sorted_unique_scores = sorted(list(set([record[1] for record in students_records])))
    if len(sorted_unique_scores) > 1:
        second_lowest_score = sorted_unique_scores[1]
        # get names of students with that score and sort alphabetically
        student_names_with_second_lowest_score = sorted([
            record[0] for record in students_records if record[1] == second_lowest_score
        ])
        if len(student_names_with_second_lowest_score):
            print(*student_names_with_second_lowest_score, sep='\n')


def execute_finding_percentage_challenge():
    """ Problem 1: Data types 4/6 """
    if __name__ == '__main__':
        n = int(input("Enter number of students: "))
        student_marks = dict()
        for _ in range(n):
            name, *line = re.split(r'\s+', input("Enter student and his grades (separated by space): "))
            print(name, line)
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input("Enter a student name: ").strip()
        if query_name in student_marks.keys():
            query_student_scores = student_marks[query_name]
            if len(query_student_scores) > 0:
                avg_query_student_score = round(sum(query_student_scores) / len(query_student_scores), 2)
                # note: reminder = 0 leads to .0 result, needs to be corrected while converting into str
                print(f"{avg_query_student_score:.2f}")


def execute_lists_challenge():
    """ Problem 1: Data types 5/6 """
    # Initializing list
    n = int(input("Enter number of command you would like to perform on a list: "))
    tmp_list = list()
    for _ in range(n):
        command_name, *command_args = input("Command: ").strip().split()
        command_args = list(map(int, command_args))
        if command_name == 'insert' and len(command_args) == 2:
            # insert i e: Insert integer  at position
            tmp_list.insert(command_args[0], command_args[1])
        elif command_name == 'print':
            # print: Print the list
            print(tmp_list)
        elif command_name == 'remove' and len(command_args) == 1:
            # remove e: Delete the first occurrence of integer
            try:
                tmp_list.remove(command_args[0])
            except ValueError:
                pass
        elif command_name == 'append' and len(command_args) == 1:
            # append e: Insert integer  at the end of the list
            tmp_list.append(command_args[0])
        elif command_name == 'sort':
            # sort: Sort the list
            tmp_list = sorted(tmp_list)
        elif command_name == 'pop':
            # pop: Pop the last element from the list
            tmp_list.pop()  # last is by default
        elif command_name == 'reverse':
            tmp_list = tmp_list[::-1]


def execute_tuples_challenge():
    """ Problem 1: Data types 6/6 """
    # _ = int(input("Enter number of elements: "))
    integer_list = re.split(r'\s+', input("Enter integers (separated by space): "))
    integer_list = list(map(int, integer_list))
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))


def swap_case(s):
    return s.swapcase()


def execute_swap_case():
    """ Problem 1: Strings 1/14 """
    s = input()
    result = swap_case(s)
    print(result)


def split_and_join(line):
    return '-'.join(line.split(' '))


def execute_split_and_join():
    """ Problem 1: Strings 2/14 """
    line = input()
    result = split_and_join(line)
    print(result)


def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")


def execute_print_full_name():
    """ Problem 1: Strings 3/14 """
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print_full_name(first_name, last_name)


def mutate_string(string, position, character):
    if position < len(string):
        composed_string = string[:position] + character
        if (position + 1) < len(string):
            composed_string += string[(position + 1):]
        return composed_string
    return string


def execute_mutate_string():
    """ Problem 1: Strings 4/14 """
    s = input("Please enter a string you want to mutate: ")
    i, c = input("Please enter index of character and a new character (separated by space): ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


def count_substring(string, sub_string):
    return len(re.findall(f"(?={sub_string})", string))


def execute_count_substring():
    """ Problem 1: Strings 5/14 """
    string = input("Please enter a string: ").strip()
    sub_string = input("Please enter a substring you would like to count: ").strip()

    count = count_substring(string, sub_string)
    print(count)


def execute_string_validator():
    """ Problem 1: Strings 6/14 """
    if __name__ == '__main__':
        s = input("Please enter a string to be validated: ")
        functions = [
            {
                'function': lambda x: x.isalnum(),
                'description': "Has any alphanumeric characters",
                'value': False
            },
            {
                'function': lambda x: x.isalpha(),
                'description': "Has any alphabetical characters",
                'value': False
            },
            {
                'function': lambda x: x.isdigit(),
                'description': "Has any digits characters",
                'value': False
            },
            {
                'function': lambda x: x.islower(),
                'description': "Has any lowercase characters",
                'value': False
            },
            {
                'function': lambda x: x.isupper(),
                'description': "Has any uppercase characters",
                'value': False
            },
        ]
        for char in s:
            for function_dict in functions:
                if not function_dict.get('value'):
                    function_dict['value'] = function_dict['function'](char)
        for function_dict in functions:
            print(f"{function_dict.get('description')}: {function_dict.get('value')}")


def execute_text_alignment():
    """ Problem 1: Strings 7/14 """

    thickness = int(input("Please enter an odd number: "))  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle BeltqA2
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


def execute_wrap():
    """ Problem 1: Strings 8/14 """
    string, max_width = input("Please enter string: "), int(input("Please enter max width: "))
    result = wrap(string, max_width)
    print(result)


def execute_designer_door_mat():
    """ Problem 1: Strings 9/14 """
    max_dimensions = input("Please enter output height and width (separated by space): ").split(' ')
    if len(max_dimensions) > 1:
        max_height, max_width = int(max_dimensions[0]), int(max_dimensions[1])
        # max_height, max_width = 11, 33
        #     ---------------.|.---------------
        #     ------------.|..|..|.------------
        #     ---------.|..|..|..|..|.---------
        #     ------.|..|..|..|..|..|..|.------
        #     ---.|..|..|..|..|..|..|..|..|.---
        #     -------------WELCOME-------------
        #     ---.|..|..|..|..|..|..|..|..|.---
        #     ------.|..|..|..|..|..|..|.------
        #     ---------.|..|..|..|..|.---------
        #     ------------.|..|..|.------------
        #     ---------------.|.---------------

        n_decorating_rows = (max_height - 1) // 2

        # Top
        for i in range(n_decorating_rows):
            print(('.|.' * (i * 2 + 1)).center(max_width, '-'))

        # Center
        print('WELCOME'.center(max_width, '-'))

        # Bottom
        for i in range(n_decorating_rows):
            print(('.|.' * ((n_decorating_rows - 1 - i) * 2 + 1)).center(max_width, '-'))


def print_formatted(number):
    bin_number = str(bin(number))[2:]
    bin_number_width = len(bin_number)
    for i in range(1, number + 1):
        bin_i = str(bin(i))[2:].rjust(bin_number_width)
        decimal_i = str(i).rjust(bin_number_width)
        oct_i = str(oct(i))[2:].rjust(bin_number_width)
        hex_i = str(hex(i))[2:].upper().rjust(bin_number_width)
        print(decimal_i, oct_i, hex_i, bin_i)


def execute_print_formatted():
    """ Problem 1: Strings 10/14 """
    n = int(input("Enter a number: "))
    print_formatted(n)


def print_rangoli(size):
    # --------e--------
    # ------e-d-e------
    # ----e-d-c-d-e----
    # --e-d-c-b-c-d-e--
    # e-d-c-b-a-b-c-d-e
    # --e-d-c-b-c-d-e--
    # ----e-d-c-d-e----
    # ------e-d-e------
    # --------e--------
    if size <= len(letters):
        if size < len(letters):
            used_letters = letters[:size]
        else:
            used_letters = letters

        max_width = (len(used_letters) - 1) * 2 * 2 + 1
        # Top
        for i in range(len(used_letters) - 1):
            used_letters_ = used_letters[::-1][:(i + 1)][::-1]
            print('-'.join((used_letters_[::-1] + used_letters_[1:])).center(max_width, '-'))

        # Center
        print('-'.join((used_letters[::-1] + used_letters[1:])).center(max_width, '-'))

        # Bottom
        for i in range(len(used_letters) - 1):
            used_letters_ = used_letters[::-1][:(len(used_letters) - 1 - i)][::-1]
            print('-'.join((used_letters_[::-1] + used_letters_[1:])).center(max_width, '-'))


def execute_print_rangoli():
    """ Problem 1: Strings 11/14 """
    n = int(input("Please enter a number: "))
    print_rangoli(n)


def solve(s):
    # title() didn't work which is silly
    return ' '.join(map(str.capitalize, s.split(' ')))


def execute_solve():
    """ Problem 1: Strings 12/14 """
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input('Enter a string to be capitalized: ')
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()


def minion_game(string):
    string = string.upper()
    # define vowels and consonants
    vowels = list('AEIOU')  # requirement
    # from string import ascii_uppercase as uppercase_letters  # could be handy to secure that letters are used
    # consonants = [letter for letter in uppercase_letters if letter not in vowels]
    # define players
    consonants_player_name = 'Stuart'
    consonants_player_score = 0
    vowels_player_name = 'Kevin'
    vowels_player_score = 0

    # simulate the game
    for i in range(len(string)):
        if string[i] in vowels:
            vowels_player_score += (len(string) - i)
        else:  # elif string[i] in consonants:
            consonants_player_score += (len(string) - i)

    # print out results
    if consonants_player_score > vowels_player_score:
        print(consonants_player_name, consonants_player_score)
    elif consonants_player_score < vowels_player_score:
        print(vowels_player_name, vowels_player_score)
    else:
        print("Draw")


def execute_minion_game():
    """ Problem 1: Strings 13/14 """
    s = input("Enter a string: ").upper()
    # s = 'BANANA'
    minion_game(s)


def merge_the_tools(string, k):
    for i in range(len(string) // k):
        print("".join(OrderedDict.fromkeys(string[(i * k):(i * k + k)])))


def execute_merge_the_tools():
    """ Problem 1: Strings 14/14 """
    string, k = input("Please enter a string: "), int(input("Please enter a number for string split: "))
    # string, k = "AABCAAADA", 3
    merge_the_tools(string, k)


def average(array) -> object:
    unique_elements = set(array)
    return sum(unique_elements) / len(unique_elements)


def execute_average():
    """ Problem 1: Sets 1/13 """
    # n = int(input("Please enter array size: "))
    arr = list(map(int, input("Please enter elements of an array (separated by spaces): ").split()))
    # arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    result = average(arr)
    print(result)


def execute_disjoint_sets():
    """ Problem 1: Sets 2/13 """
    # sizes = list(map(int, input().split()))  # 3 2
    # arr_size, set_size = sizes[:2]
    arr = list(map(int, input("Please enter elements of an array (separated by spaces): ").split()))  # 1 5 3
    set_a = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 3 1
    set_b = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 5 7
    # Considering matching elements as success for set A and failure for set B respectively
    print(sum([int(el in set_a) - int(el in set_b) for el in arr]))


def execute_symmetric_difference():
    """ Problem 1: Sets 3/13 """
    # set_1_size = int(input())  # 4
    set_1 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 2 4 5 9
    # set_2_size = int(input())  # 4
    set_2 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 2 4 11 12
    for i in sorted(set_1.symmetric_difference(set_2)):
        print(i)  # 5 9 11 12


def execute_set_add():
    """ Problem 1: Sets 4/13 """
    n_countries = int(input("Please enter number of countries you would like to consider: "))
    unique_countries = set()
    for i in range(n_countries):
        unique_countries.add(input("Please enter a name of country: "))
    print(len(unique_countries))


def execute_sets_commands():
    """ Problem 1: Sets 5/13 """
    _ = int(input("Enter number of elements in a set: "))  # 9
    s = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 1 2 3 4 5 6 7 8 9
    n = int(input("Enter number of commands you would like to perform on a set: "))  # 10
    for _ in range(n):
        command_name, *command_args = input("Command: ").strip().split()
        command_args = list(map(int, command_args))
        if command_name == 'remove' and len(command_args) == 1:
            # remove e: Delete an element from a set
            try:
                s.remove(command_args[0])
            except ValueError:
                pass
        elif command_name == 'discard' and len(command_args) == 1:
            # discard e: Delete an element from a set without raising an error
            s.discard(command_args[0])
        elif command_name == 'pop':
            try:
                # Pop an element from a set
                s.pop()
            except KeyError:
                pass
    print(sum(s))


def execute_sets_union():
    """ Problem 1: Sets 6/13 """
    # _ = int(input("Enter number of elements in a set: "))  # 9
    s1 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 1 2 3 4 5 6 7 8 9
    # _ = int(input("Enter number of elements in a set: ")) # 9
    s2 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 10 1 2 3 11 21 55 6 8
    print(len(s1.union(s2)))


def execute_sets_intersection():
    """ Problem 1: Sets 7/13 """
    _ = int(input())  # "Enter number of elements in a set: "  # 9
    s1 = set(map(int, input().split()))  # "Please enter elements of a set (sep by spaces): "  # 1 2 3 4 5 6 7 8 9
    _ = int(input())  # "Enter number of elements in a set: "  # 9
    s2 = set(map(int, input().split()))  # "Please enter elements of a set (sep by spaces): "  # 10 1 2 3 11 21 55 6 8
    print(len(s1.intersection(s2)))


def execute_sets_difference():
    """ Problem 1: Sets 8/13 """
    # _ = int(input("Enter number of elements in a set: "))  # 9
    s1 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 1 2 3 4 5 6 7 8 9
    # _ = int(input("Enter number of elements in a set: ")) # 9
    s2 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 10 1 2 3 11 21 55 6 8
    print(len(s1.difference(s2)))


def execute_sets_symmetric_difference():
    """ Problem 1: Sets 9/13 """
    # _ = int(input("Enter number of elements in a set: "))  # 9
    s1 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 1 2 3 4 5 6 7 8 9
    # _ = int(input("Enter number of elements in a set: ")) # 9
    s2 = set(map(int, input("Please enter elements of a set (separated by spaces): ").split()))  # 10 1 2 3 11 21 55 6 8
    print(len(s1.symmetric_difference(s2)))


def execute_sets_mutations():
    """ Problem 1: Sets 10/13 """
    _ = int(input())  # "Enter number of elements in a set: "
    s = set(map(int, input().split()))  # "Please enter elements of a set (separated by spaces): "
    n = int(input())  # "Enter number of commands you would like to perform on a set: "
    for _ in range(n):
        command_name, _ = input().strip().split()  # "Command: "
        command_set = set(map(int, input().split()))  # set to apply a command with
        if command_name == 'update':
            s.update(command_set)
        elif command_name == 'intersection_update':
            s.intersection_update(command_set)
        elif command_name == 'difference_update':
            s.difference_update(command_set)
        elif command_name == 'symmetric_difference_update':
            s.symmetric_difference_update(command_set)

    print(sum(s))


def execute_find_captain_room_challenge():
    """ Problem 1: Sets 11/13 """
    # _ = int(input("Enter number of people in a group: ").strip())  # useless
    # unordered rooms list, example: 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
    rooms_list = re.split(r'\s+', input("Enter list of booked rooms (numbers are separated by space): "))
    rooms_list = list(map(int, rooms_list))
    counter = Counter(rooms_list)
    captain_room = counter.most_common()[-1][0]
    print(captain_room)


def execute_check_subset():
    """ Problem 1: Sets 12/13 """
    # The third line of each test case contains the number of elements in set .
    # The fourth line of each test case contains the space separated elements of set .
    n = int(input())  # "Enter number of test cases: "
    for _ in range(n):
        _ = int(input())  # "Enter number of elements in a set: "
        s1 = set(map(int, input().split()))  # "Please enter elements of a set (separated by spaces): "
        _ = int(input())  # "Enter number of elements in a set: "
        s2 = set(map(int, input().split()))  # "Please enter elements of a set (separated by spaces): "
        print(s1.issubset(s2))


def execute_check_strict_superset():
    """ Problem 1: Sets 13/13 """
    s = set(map(int, input().split()))  # "Please enter elements of a set (separated by spaces): "
    n = int(input())  # "Enter number of sets: "
    res = True
    for _ in range(n):
        s_i = set(map(int, input().split()))  # "Please enter elements of a set (separated by spaces): "
        res = s.issuperset(s_i)
        if not res:
            break
    print(res)


def execute_collections_counter():
    """ Problem 1: Collections 1/8 """
    _ = int(input())  # "Enter number of shoes: "
    shoe_sizes = Counter(map(int, input().split()))  # "Please enter shoe sizes of the shop (separated by spaces): "
    n_customers = int(input())  # "Enter number of customers: "
    money_earned = 0
    for _ in range(n_customers):
        # "Please enter shoe size and price (separated by spaces): "
        shoe_size, shoe_price = list(map(int, input().split()))
        if shoe_sizes[shoe_size]:
            money_earned += shoe_price
            shoe_sizes[shoe_size] -= 1
    print(money_earned)


def execute_default_dict():
    """ Problem 1: Collections 2/8 """
    n, m = list(map(int, input().split()))  # "Enter M and N separated by space: "
    content_dict = defaultdict(list)
    for i in range(1, n + 1):
        # collect words for A and their places
        content_dict[input()].append(i)
    for _ in range(m):
        # check if a word has appeared in A
        b_word = input()
        if content_dict[b_word]:
            print(" ".join(map(str, content_dict[b_word])))
        else:
            print(-1)


def execute_named_tuple():
    """ Problem 1: Collections 3/8 """
    # example:
    # Point = namedtuple('Point','x,y')
    # >>> pt1 = Point(1,2)
    # >>> pt2 = Point(3,4)
    # >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
    # The first line contains an integer , the total number of students.
    # The second line contains the names of the columns in any order.
    # The next  lines contains the , ,  and , under their respective column names.
    # 5
    # ID         MARKS      NAME       CLASS
    # 1          97         Raymond    7
    # 2          50         Steven     4
    # 3          91         Adrian     9
    # 4          72         Stewart    5
    # 5          80         Peter      6
    n_records = int(input())  # "Enter number of rows of a spreadsheet: "
    # "Enter names of the columns in any order: "  # columns are fixed to be ID, MARKS, NAME, CLASS but order may change
    Record = namedtuple('Record', ','.join(input().split()))
    avg_grade = 0
    for record_i in range(n_records):
        avg_grade += int(Record(*input().split()).MARKS)
    print(avg_grade / n_records)


def execute_ordered_dict():
    """ Problem 1: Collections 4/8 """
    n = int(input())  # "Enter number of items: "
    shop_dict = OrderedDict()
    for _ in range(n):
        item_name, item_price = input().rsplit(' ', maxsplit=1)  # "Enter item name and price space separated: "
        if item_name not in shop_dict.keys():
            shop_dict[item_name] = 0
        shop_dict[item_name] += int(item_price)
    for k, v in shop_dict.items():
        print(k, v)


def execute_word_order():
    """ Problem 1: Collections 5/8 """
    # On the first line, output the number of distinct words from the input.
    # On the second line, output the number of occurrences for each distinct word according to their appearance.
    n = int(input())  # "Enter number of items: "
    words_counter = Counter()
    for _ in range(n):
        words_counter.update(Counter([input()]))  # "Enter a word: "
    print(len(words_counter))
    print(' '.join(map(str, list(dict(words_counter).values()))))


def execute_deque():
    """ Problem 1: Collections 6/8 """
    n = int(input())  # "Enter number of commands you would like to perform on a deque: "
    tmp_deque = deque()
    for _ in range(n):
        command_name, *command_args = input().strip().split()  # "Command: "
        command_args = list(map(int, command_args))
        if command_name == 'append' and len(command_args) == 1:
            # append e: Append an element
            tmp_deque.append(command_args[0])
        elif command_name == 'pop':
            # pop: Pop an element
            tmp_deque.pop()
        elif command_name == 'popleft':
            # popleft: Pop an element from the left
            tmp_deque.popleft()
        elif command_name == 'appendleft' and len(command_args) == 1:
            # appendleft e: Append an element to the left
            tmp_deque.appendleft(command_args[0])
    print(' '.join(map(str, tmp_deque)))


def execute_company_logo():
    """ Problem 1: Collections 7/8 """
    input_letters = sorted(input())  # "Enter number of items: "
    common_letters_counter = dict(Counter(input_letters).most_common(3))
    for letter, counter in common_letters_counter.items():
        print(f"{letter} {counter}")


def execute_piling_up():
    """ Problem 1: Collections 8/8 """
    for _ in range(int(input())):
        _, cubes_queue = input(), deque(map(int, input().split()))

        for cube_i in reversed(sorted(cubes_queue)):
            if cubes_queue[-1] == cube_i:
                cubes_queue.pop()
            elif cubes_queue[0] == cube_i:
                cubes_queue.popleft()
            else:
                print('No')
                break
        else:
            print('Yes')


def execute_calendar_module():
    """ Problem 1: Date and Time 1/2 """
    # NOTE: print(calendar.TextCalendar(firstweekday=6).formatyear(2020)) -> prints the whole calendar, handy
    month, day, year = map(int, input().split())  # MM DD YYYY
    print(calendar.day_name[calendar.weekday(year=year, month=month, day=day)].upper())


def time_delta(t1: str, t2: str):
    # Examples:
    # Sun 10 May 2015 13:54:36 -0700
    # Sun 10 May 2015 13:54:36 -0000
    # Sat 02 May 2015 19:54:36 +0530
    # Fri 01 May 2015 13:54:36 -0000
    input_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, input_format)
    t2 = datetime.strptime(t2, input_format)
    diff = int(abs((t2 - t1).total_seconds()))
    return diff


def execute_time_delta():
    """ Problem 1: Date and Time 2/2 """
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
        # fptr.write(delta + '\n')
    # fptr.close()


def execute_exceptions():
    """ Problem 1: Exceptions 1/1 """
    n = int(input())
    for _ in range(n):
        try:
            a, b = list(map(int, input().split()))
            print(a // b)
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)


def execute_zipped():
    """ Problem 1: Built-ins 1/3 """
    _, n_records = list(map(int, input().split()))
    grades = list()
    for _ in range(n_records):
        grades.append(list(map(float, input().split())))

    for i in zip(*grades):
        print(sum(i) / len(i))


def execute_athlete_sort():
    """ Problem 1: Built-ins 2/3 """
    n, _ = list(map(int, input().split()))

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for record in sorted(arr, key=lambda x: x[k]):
        print(*record)


def execute_sorting():
    """ Problem 1: Built-ins 3/3 """
    print(
        *sorted(input(), key=(ascii_letters + '1357902468').index),
        sep=''
    )


def execute_map_and_lambda():
    """ Problem 1: Python Functionals 1/1 """
    cube = lambda x: x ** 3

    def fibonacci(n):
        # return a list of fibonacci numbers
        numbers = [0, 1]
        for _ in range(n - 2):
            numbers.append(sum(numbers[-2:]))
        return numbers[:n]

    print(list(map(cube, fibonacci(int(input())))))


def execute_detect_floating_point_number():
    """ Problem 1: Regex and Parsing challenges 1/17 """
    for _ in range(int(input())):
        print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', input())))


def execute_re_split():
    """ Problem 1: Regex and Parsing challenges 2/17 """
    regex_pattern = r",|\."
    print("\n".join(re.split(regex_pattern, input())))


def execute_re_groups():
    """ Problem 1: Regex and Parsing challenges 3/17 """
    # Exmaples:
    # >>> import re
    # >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@HR.com')
    # >>> m.group(0)       # The entire match
    # 'username@HR.com'
    # >>> m.group(1)       # The first parenthesized subgroup.
    # 'username'
    # >>> m.group(2)       # The second parenthesized subgroup.
    # 'HR'
    # >>> m.group(3)       # The third parenthesized subgroup.
    # 'com'
    # >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
    # ('username', 'HR', 'com')
    # >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@HR.com')
    # >>> m.groups()
    # ('username', 'HR', 'com')
    # >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@HR.com')
    # >>> m.groupdict()
    # {'website': 'HR', 'user': 'myname', 'extension': 'com'}
    m = re.search(r'([a-zA-Z0-9])\1+', input())
    print(m.group(1) if m else -1)


def execute_re_find_all():
    """ Problem 1: Regex and Parsing challenges 4/17 """
    # Example: 
    # map(lambda x: x.group(),re.finditer(r'\w','http: //www.HR.com/'))
    # ['h', 't', 't', 'p', 'w', 'w', 'w', 'H', 'R']
    vowels = 'aeiou'
    consonants = ''.join(set(letters) - set(vowels))
    a = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), input(), re.IGNORECASE)
    print('\n'.join(a or ['-1']))


def execute_re_start():
    """ Problem 1: Regex and Parsing challenges 5/17 """
    input_string, pattern = input(), input()
    pattern_shift = len(pattern) - 1
    found_matches = list(re.finditer(r'(?={})'.format(pattern), input_string))
    if found_matches:
        print('\n'.join(str((m.start(), m.start() + pattern_shift)) for m in found_matches))
    else:
        print('(-1, -1)')


def execute_re_substitution():
    """ Problem 1: Regex and Parsing challenges 6/17 """
    n = int(input())
    for _ in range(n):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))


def execute_re_roman_numerals():
    """ Problem 1: Regex and Parsing challenges 7/17 """
    regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"
    print(str(bool(re.match(regex_pattern, input()))))


def execute_re_validate_phone_numbers():
    """ Problem 1: Regex and Parsing challenges 8/17 """
    n = int(input())
    for _ in range(n):
        print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO')


def execute_re_validate_emails():
    """ Problem 1: Regex and Parsing challenges 9/17 """
    n = int(input())
    for _ in range(n):
        name, addr = email.utils.parseaddr(input())
        if bool(re.match(r'[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$', addr)):
            print(email.utils.formataddr((name, addr)))


def execute_hex_color_code():
    """ Problem 1: Regex and Parsing challenges 10/17 """
    n = int(input())
    pattern = r'[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})'
    for _ in range(n):
        line = input()
        for i in re.findall(pattern, line, re.IGNORECASE):
            print(i)


class HTMLParser(DefaultHTMLParser, ABC):

    def handle_starttag(self, tag, attrs):
        print(f"{'Start':<6}: {tag}")
        self.print_attributes(attrs)

    def handle_endtag(self, tag):
        print(f"{'End':<6}: {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"{'Empty':<6}: {tag}")
        self.print_attributes(attrs)

    @staticmethod
    def print_attributes(attrs):
        attrs = attrs or list()
        for attr_class, attr_value in attrs:
            print(f"-> {attr_class} > {attr_value}")


def execute_html_parser():
    """ Problem 1: Regex and Parsing challenges 11/17 """
    # read inputs
    lines = '\n'.join([input() for _ in range(int(input()))])
    # feed parser
    parser = HTMLParser()
    parser.feed(lines)
    parser.close()


class HTMLParserWithComment(DefaultHTMLParser, ABC):

    def handle_comment(self, data):
        n_lines = len(data.split('\n'))
        if n_lines > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


def execute_html_parser_comment():
    """ Problem 1: Regex and Parsing challenges 12/17 """
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = HTMLParserWithComment()
    parser.feed(html)
    parser.close()


class HTMLParserDetector(DefaultHTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attributes(attrs)

    @staticmethod
    def print_attributes(attrs):
        attrs = attrs or list()
        for attr_class, attr_value in attrs:
            print(f"-> {attr_class} > {attr_value}")


def execute_html_parser_detector():
    """ Problem 1: Regex and Parsing challenges 13/17 """
    html = '\n'.join([input() for _ in range(int(input()))])
    parser = HTMLParserDetector()
    parser.feed(html)
    parser.close()


def execute_validate_uid():
    """ Problem 1: Regex and Parsing challenges 14/17 """
    patterns = [
        r'[A-Za-z0-9]{10}',
        r'([A-Z].*){2}',
        r'([0-9].*){3}'
    ]
    for _ in range(int(input())):
        uid = input()
        is_valid = True
        for pattern in patterns:
            if is_valid:
                is_valid = bool(re.search(pattern, uid))
                if not is_valid:
                    break
        if is_valid and bool(re.search(r'.*(.).*\1', uid)):
            is_valid = False
        print('Valid' if is_valid else 'Invalid')


def execute_validate_cards_numbers():
    """ Problem 1: Regex and Parsing challenges 15/17 """
    for _ in range(int(input())):
        if re.match(r"^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$", input()):
            print("Valid")
        else:
            print("Invalid")


def execute_postal_codes():
    """ Problem 1: Regex and Parsing challenges 16/17 """
    regex_integer_in_range = r"^[1-9][\d]{5}$"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
    pattern = input()
    print(
        bool(re.match(regex_integer_in_range, pattern))
        and len(re.findall(regex_alternating_repetitive_digit_pair, pattern)) < 2
    )


def execute_matrix_script():
    """ Problem 1: Regex and Parsing challenges 17/17 """
    first_multiple_input = input().rstrip().split()

    n, m = map(int, first_multiple_input)

    matrix = []
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    matrix = ''.join([''.join(mi) for mi in zip(*matrix)])
    print(re.sub(r'\b[^a-zA-Z\d]+\b', r' ', matrix))


def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)


def execute_xml_score():
    """ Problem 1: XML challenges 1/2 """
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


def execute_xml_max_depth():
    """ Problem 1: XML challenges 2/2 """
    maxdepth = 0

    def depth(elem, level):
        global maxdepth
        if level == maxdepth:
            maxdepth += 1

        for sub_elem in elem:
            depth(sub_elem, level + 1)

    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


def wrapper(f):
    def fun(l):
        f([f"+91 {li[-10:-5]} {li[-5:]}" for li in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


def execute_decorator_phone():
    """ Problem 1: Closures and Decorations challenges 1/2 """
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


def person_lister(f):
    def inner(people):
        # 2nd is age, sorting ascending
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner


@person_lister
def name_format(person):
    # prefix name last name
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


def execute_decorator_name():
    """ Problem 1: Closures and Decorations challenges 2/2 """
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


if __name__ == '__main__':
    # Problem 1: Introduction
    # execute_say_hello_world_challenge()
    # execute_python_if_else_challenge()
    # execute_arithmetic_operators_challenge()
    # execute_numbers_division_challenge()
    # execute_loops_challenge()
    # execute_function_is_leap_challenge()
    # execute_print_function_challenge()

    # Problem 1: Data types
    # execute_lists_comprehension_challenge()
    # execute_runner_up_score_challenge()
    # execute_nested_lists_challenge()
    # execute_finding_percentage_challenge()
    # execute_lists_challenge()
    # execute_tuples_challenge()

    # Problem 1: Strings
    # execute_swap_case()
    # execute_split_and_join()
    # execute_print_full_name()
    # execute_mutate_string()
    # execute_count_substring()
    # execute_string_validator()
    # execute_text_alignment()
    # execute_wrap()
    # execute_designer_door_mat()
    # execute_print_formatted()
    # execute_print_rangoli()
    # execute_solve()
    # execute_minion_game()
    # execute_merge_the_tools()

    # Problem 1: Sets
    # execute_average()
    # execute_disjoint_sets()
    # execute_symmetric_difference()
    # execute_set_add()
    # execute_sets_commands()
    # execute_sets_union()
    # execute_sets_intersection()
    # execute_sets_difference()
    # execute_sets_symmetric_difference()
    # execute_sets_mutations()
    # execute_find_captain_room_challenge()
    # execute_check_subset()
    # execute_check_strict_superset()

    # Problem 1: Collections
    # execute_collections_counter()
    # execute_default_dict()
    # execute_named_tuple()
    # execute_ordered_dict()
    # execute_word_order()
    # execute_deque()
    # execute_company_logo()
    # execute_piling_up()

    # Problem 1: Date and Time
    # execute_calendar_module()
    # execute_time_delta()

    # Problem 1: Exceptions
    # execute_exceptions()

    # Problem 1: Built-ins
    # execute_zipped()
    # execute_athlete_sort()
    # execute_sorting()

    # Problem 1: Python Functionals
    # execute_map_and_lambda()

    # Problem 1: Regex and Parsing challenges
    # execute_detect_floating_point_number()
    # execute_re_split()
    # execute_re_groups()
    # execute_re_find_all()
    # execute_re_start()
    # execute_re_substitution()
    # execute_re_roman_numerals()
    # execute_re_validate_phone_numbers()
    # execute_re_validate_emails()
    # execute_hex_color_code()
    # execute_html_parser()
    # execute_html_parser_comment()
    # execute_html_parser_detector()
    # execute_validate_uid()
    # execute_validate_cards_numbers()
    # execute_postal_codes()
    # execute_matrix_script()

    # Problem 1: XML challenges
    # execute_xml_score()
    # execute_xml_max_depth()

    # Problem 1: Closures and Decorations challenges
    # execute_decorator_phone()
    # execute_decorator_name()

    # Problem 1: numpy challenges
    pass