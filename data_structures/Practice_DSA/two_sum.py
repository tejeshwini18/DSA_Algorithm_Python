def two_sum(nums, target):
    num_to_index = {}  # A dictionary to store numbers and their indices
    for index, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        if complement in num_to_index:  # Check if the complement exists
            return [num_to_index[complement], index]
        num_to_index[num] = index  # Store the current number and its index
    return []  # Return an empty list if no solution is found


# Test cases
print(two_sum([5, 1, 7, 2, 9, 3], 10))  # [1, 4]
print(two_sum([4, 2, 11, 7, 6, 3], 9))  # [1, 3]
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  # [0, 3]
print(two_sum([1, 3, 5, 7, 9], 10))  # [1, 3]
print(two_sum([1, 2, 3, 4, 5], 10))  # []
print(two_sum([1, 2, 3, 4, 5], 7))  # [2, 3]
print(two_sum([1, 2, 3, 4, 5], 3))  # [0, 1]
print(two_sum([], 0))  # []
