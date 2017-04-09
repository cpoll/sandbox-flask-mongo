from .fizzbuzz_helper import get_fizzbuzz_range


def test_fizzbuzz_thirty():
    expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
                11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
                "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz"]

    assert get_fizzbuzz_range(30) == expected


def test_fizzbuzz_one():
    assert get_fizzbuzz_range(1) == [1]


def test_fizzbuzz_zero_returns_empty_list():
    assert get_fizzbuzz_range(0) == []


def test_fizzbuzz_negative_returns_empty_list():
    assert get_fizzbuzz_range(-1) == []


def test_fizzbuzz_string_returns_empty_list():
    assert get_fizzbuzz_range("hello") == []

