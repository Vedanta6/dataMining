#!/usr/bin/env python
import re
import textwrap
from string import ascii_lowercase as letters
from collections import Counter, OrderedDict


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


def execute_find_captain_room_challenge():
    """ Problem 1: Was not in the Introduction """
    # _ = int(input("Enter number of people in a group: ").strip())  # useless
    # unordered rooms list, example: 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
    rooms_list = re.split(r'\s+', input("Enter list of booked rooms (numbers are separated by space): "))
    rooms_list = list(map(int, rooms_list))
    counter = Counter(rooms_list)
    captain_room = counter.most_common()[-1][0]
    print(captain_room)


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
            if query_student_scores > 0:
                avg_query_student_score = round(sum(query_student_scores) / len(query_student_scores), 2)
                # note: reminder = 0 leads to .0 result, needs to be corrected while converting into str
                print(f"{avg_query_student_score:.2f}")


def execute_lists_challenge():
    """ Problem 1: Data types 5/6 """
    # Initializing list
    N = int(input("Enter number of command you would like to perform on a list: "))
    tmp_list = list()
    for _ in range(N):
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
            print(('.|.' * ((n_decorating_rows - 1 - i) * 2 + 1) ).center(max_width, '-'))


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


if __name__ == '__main__':
    # Problem 1: Introduction
    # execute_say_hello_world_challenge()
    # execute_python_if_else_challenge()
    # execute_arithmetic_operators_challenge()
    # execute_numbers_division_challenge()
    # execute_loops_challenge()
    # execute_function_is_leap_challenge()
    # execute_print_function_challenge()
    # execute_find_captain_room_challenge()

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
    execute_merge_the_tools()
