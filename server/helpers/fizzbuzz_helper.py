__MAX_ALLOWED_FIZZBUZZ_NUMBER = 100000

def get_fizzbuzz_range(number):
    """
    Get an array of fizzbuzz values from 1 to number (inclusive)
    or empty array if the number is invalid
    """

    if not isinstance(number, int) or number < 1 or number > __MAX_ALLOWED_FIZZBUZZ_NUMBER:
        return []

    return list(map(get_fizzbuzz_value, range(1, number+1)))

def get_fizzbuzz_value(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
