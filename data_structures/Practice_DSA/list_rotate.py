def rotate(nums,k):
    if k<=0:
        return None
    j=len(nums)
    k %= j
    nums.reverse()
    nums[:k]=nums[:k][::-1]
    nums[k:]=nums[k:][::-1]
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""