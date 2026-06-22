# Merge Overlapping Intervals
# Input:
# [(1,3), (2,6), (8,10), (9,15)]
# Output:
# [(1,6), (8,15)]


def merge_interval(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    
    for start,end in intervals[1:]:
        last_start,last_end = result[-1]
        
        if start <= last_end:
            result[-1] = (last_start,max(last_end,end))
        else:
            result.append((start,end))
    return result

print("**************Test Case 1**************")   
print(merge_interval([]))
print("**************Test Case 2**************")   
print(merge_interval([(1, 3), (2, 4), (6, 8), (9, 10)]))
print("**************Test Case 3**************")   
print(merge_interval([(1, 3), (2, 6), (8, 10), (9, 15)]))
print("**************Test Case 4**************")   
print(merge_interval([(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)]))
print("**************Test Case 5**************")   
print(merge_interval([(1, 4), (4, 5)]))
print("**************Test Case 6**************")   
print(merge_interval([(1, 4), (5, 6)]))
print("**************Test Case 7**************")   
print(merge_interval([(1, 4), (6, 8)]))
print("**************Test Case 8**************")   
print(merge_interval([(1, 4), (8, 10)]))
print("**************Test Case 9**************")   
print(merge_interval([(1, 4), (10, 12)]))
print("**************Test Case 10**************")   
print(merge_interval([(1, 4), (12, 14)]))