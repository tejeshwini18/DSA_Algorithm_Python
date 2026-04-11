def is_perfect_number(n):
    '''
    A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
    For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7, and 14, and their sum is 28.
    Time Complexity**: O(sqrt(n))
    Space Complexity**: O(1)
    '''
    if n < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
    return sum_of_divisors == n

print(is_perfect_number(28))
print(is_perfect_number(35))
print(is_perfect_number(36))    
print(is_perfect_number(123))
print(is_perfect_number(496))