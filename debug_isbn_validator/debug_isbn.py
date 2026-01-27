def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[: length - 1]
    given_check_digit = isbn[length - 1].upper()

    try:
        main_digits_list = [int(d) for d in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    if length == 10:
        # ISBN-10 check digit can be 0-9 or X only
        if not (given_check_digit.isdigit() or given_check_digit == 'X'):
            print('Invalid character was found.')
            return

        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        # ISBN-13 check digit must be numeric
        if not given_check_digit.isdigit():
            print('Invalid character was found.')
            return

        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    if result == 10:
        return 'X'
    return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    return str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    try:
        isbn, length_str = user_input.split(',')
    except ValueError:
        print('Enter comma-separated values.')
        return

    isbn = isbn.strip()
    length_str = length_str.strip()

    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# main()

