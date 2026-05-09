input_list = [[1,2], [2,3], [1, 2], [2,3], [4,5]]

unique_list = set()

for val in input_list:
    item_val = tuple(val)
    if item_val in unique_list:
        print(item_val)
    else:
        unique_list.add(item_val)
print(unique_list)