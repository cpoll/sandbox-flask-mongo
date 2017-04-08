from .fizzbuzz_helper import get_fizzbuzz_range

def test_fizzbuzz_positive_integer():
    expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
                11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
                "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz"]

    assert get_fizzbuzz_range(30) == expected
