
# Goldbach's Conjecture Solver

A Python implementation that finds all pairs of prime numbers that sum to a given even number, demonstrating Goldbach's Conjecture.

## About Goldbach's Conjecture

Goldbach's Conjecture is one of the oldest unsolved problems in number theory and mathematics. It states that every even integer greater than 2 can be expressed as the sum of two prime numbers.

**Examples:**
- 4 = 2 + 2
- 6 = 3 + 3
- 8 = 3 + 5
- 10 = 3 + 7 = 5 + 5

## Features

- **Prime Number Detection**: Efficient primality testing using square root optimization
- **Pair Generation**: Finds all unique prime pairs that sum to the target number
- **Input Validation**: Exception handling for invalid inputs
- **Comprehensive Output**: Lists all valid prime pair combinations

## Usage

### Running the Program
```bash
python goldbach.py
```

### Example Sessions

#### Successful Case
Enter an even number greater than 2: 10  
The number 10 equals to the sum of 3 and 7  
The number 10 equals to the sum of 5 and 5

#### Multiple Pairs
Enter an even number greater than 2: 20  
The number 20 equals to the sum of 3 and 17  
The number 20 equals to the sum of 7 and 13

#### Invalid Input
Enter an even number greater than 2: abc  
Invalid input: invalid literal for int() with base 10: 'abc'

## Functions

### `is_prime(n)`
Determines if a number is prime using trial division up to the square root.

**Parameters:**
- `n` (int): Number to check for primality

**Returns:**
- `bool`: True if prime, False otherwise

**Time Complexity:** O(√n)

### `sum_of_two_primes(number)`
Finds all pairs of prime numbers that sum to the given number.

**Parameters:**
- `number` (int): Target sum (should be even and > 2)

**Returns:**
- `list of tuples`: All prime pairs (x, y) where x + y = number

**Example:**
sum_of_two_primes(10) # Returns [(3, 7), (5, 5)]

## Algorithm Explanation

1. **Primality Test**: Uses trial division optimization
   - Checks divisibility only up to √n
   - Returns early on first found divisor
   - Handles edge cases (n < 2)

2. **Pair Finding**:
   - Iterates from 2 to number/2
   - For each x, calculates y = number - x
   - Checks if both x and y are prime
   - Avoids duplicate pairs by limiting search to half the number

## Requirements

- Python 3.6 or higher

## Further Enhancements

- **Sieve of Eratosthenes**: Pre-generate primes for faster lookups with large numbers
- **Caching**: Memoize prime results to avoid redundant calculations
- **Range Support**: Find Goldbach pairs for multiple numbers
- **Visualization**: Display results in a table or graph format
- **Performance Metrics**: Add timing for algorithm analysis
- **Unit Tests**: Implement comprehensive test coverage

## Mathematical Notes

- The conjecture has been verified for all even numbers up to 4 × 10^18
- While unproven, no counterexample has ever been found
- For very large numbers, the number of valid pairs tends to increase

## Performance

- **Time Complexity**: O(n√n) where n is the input number
- **Space Complexity**: O(k) where k is the number of valid pairs

## License

This project is licensed under the MIT License - see below for details:


