def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(is_power_of_two(1))
print(is_power_of_two(2))
print(is_power_of_two(3))
print(is_power_of_two(4))
print(is_power_of_two(5))
print(is_power_of_two(6))
print(is_power_of_two(7))
print(is_power_of_two(8))
print(is_power_of_two(9))
print(is_power_of_two(10))