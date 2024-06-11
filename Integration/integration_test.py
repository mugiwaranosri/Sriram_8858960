# integration_test.py
# Function 1: Check if a number is even
def is_even(num):
    return num % 2 == 0
# Integration test cases for is_even
def test_is_even_positive():
    assert is_even(2) == True  # This test should pass
def test_is_even_negative():
    assert is_even(3) == True  # This test should fail

# Function 2: Check if a number is positive
def is_positive(num):
    return num > 0
# Integration test cases for is_positive
def test_is_positive_positive():
    assert is_positive(5) == True  # This test should pass
def test_is_positive_negative():
    assert is_positive(-3) == True  # This test should fail

# Function 3: Check if a number is a prime number
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
# Integration test cases for is_prime
def test_is_prime_positive():
    assert is_prime(7) == True  # This test should pass
def test_is_prime_negative():
    assert is_prime(4) == True  # This test should fail
