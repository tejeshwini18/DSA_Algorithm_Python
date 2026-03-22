def second_largest_num(nums):
    if len(nums) < 2:
        return None

    first_large = second_large = float('-inf')

    for num in nums:
        if num > first_large:
            second_large = first_large
            first_large = num
        elif first_large > num > second_large:
            second_large = num

    return second_large if second_large != float('-inf') else None


arr1 = [96,76,30,15,6,9,45,24,64,32,88]
print(second_largest_num(arr1))

arr2 = [12, 45, 1, 23, 45, 67]
print(second_largest_num(arr2))


