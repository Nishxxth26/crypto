import random

def power(a, b, m):
    """Efficiently calculates (a^b) % m using modular exponentiation."""
    return pow(a, b, m) # Python's built-in pow() is optimized for this

def miller_rabin(n, k=10):
    
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Factor (n - 1) as 2^s * d, where d is odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        # Choose a random base 'a' such that 2 <= a <= n-2
        a = random.randint(2, n - 2)
        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue
        
        # Check for non-trivial square roots
        for _ in range(s - 1):
            x = power(x, 2, n)
            if x == 1:
                return False # Found a non-trivial square root, n is composite
            if x == n - 1:
                break # Condition satisfied, proceed to next iteration
        else:
            return False # Neither condition was met, n is composite

    return True # Passed all k tests, n is probably prime

# Example usage:
number_to_test = 101
if miller_rabin(number_to_test):
    print(f"{number_to_test} is probably prime.")
else:
    print(f"{number_to_test} is composite.")
