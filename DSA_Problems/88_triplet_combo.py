# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]



def tripletsum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        
        left = i+1 
        right = len(nums)-1

        while left<right:
            total = nums[i] + nums[left] + nums[right]

            out = [nums[i] , nums[left] , nums[right]]

            if total==0:
                result.append(out)
            left += 1
            right -= 1

            while left<right and nums[left] == nums[left-1]:
                left += 1

            while left<right and nums[right] == nums[right-1]:
                right -= 1
        if total < 0:
            left += 1
        else:
            right -= 1
    return result

input_nums = [-1,0,1,2,-1,-4]
output = tripletsum(input_nums)
print(output)

# Output: [[-1,-1,2],[-1,0,1]]
