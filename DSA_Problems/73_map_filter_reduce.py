fruit = ["Apple", "Banana", "Pear"]
map_object = map(lambda s: s[0] == "A", fruit)
print(list(map_object)) 



filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object)) 



from functools import reduce
nums = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, nums))
print("With an initial value: " + str(reduce(lambda x, y: x + y, nums, 10)))
