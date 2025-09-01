# prime_checker.py

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    test_numbers = [2, 3, 4, 17, 20, 23, 50, 97]
    print("Prime Number Checker")
    for n in test_numbers:
        print(f"{n} is {'Prime' if is_prime(n) else 'Not Prime'}")
