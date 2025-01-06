def longest_consecutive_sequence(nums):
    if len(nums)==0:
        return 0
    nums = sorted(set(nums))  # Remove duplicates and sort the numbers
    longest = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:  # Consecutive numbers
            current_streak += 1
        else:  # Sequence breaks
            longest = max(longest, current_streak)
            current_streak = 1

    # Final check for the last streak
    return max(longest, current_streak)

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""