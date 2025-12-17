def is_prime(n):
    """Check if n is prime using trial division up to square root.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_two_primes(number):
    """Return a list of all prime pairs (x, y) that sum to 'number'.

    Args:
        number (int): Target sum (should be even and > 2)

    Returns:
        list: List of tuples containing prime pairs that sum to number
    """
    pairs = []
    for x in range(2, number // 2 + 1):
        y = number - x
        if is_prime(x) and is_prime(y):
            pairs.append((x, y))
    return pairs


def validate_input(number):
    """Validate that input meets Goldbach's conjecture requirements.

    Args:
        number (int): Number to validate

    Raises:
        ValueError: If number is not even or not greater than 2
    """
    if number <= 2:
        raise ValueError("Number must be greater than 2")
    if number % 2 != 0:
        raise ValueError(
            "Number must be even (Goldbach's conjecture applies to even numbers)"
        )


def main():
    """Main entry point for the Goldbach's Conjecture solver."""
    try:
        number = int(input("Enter an even number greater than 2: "))
        validate_input(number)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    result = sum_of_two_primes(number)
    if result:
        for x, y in result:
            print(f"The number {number} equals to the sum of {x} and {y}")
    else:
        print(f"The number {number} cannot be expressed as sum of two primes")


if __name__ == "__main__":
    main()
