def find_pairs(arr1,arr2,target):
    sum_dict = {}
    for num1 in arr1:
        sum_dict[target-num1] = num1
    sum_pair =  []
    for num2 in arr2:
        if num2 in sum_dict:
            sum_pair.append((sum_dict[num2],num2))
    return sum_pair
        




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""