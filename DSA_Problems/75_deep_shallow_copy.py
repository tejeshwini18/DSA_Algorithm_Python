import copy

list1 = [1, 2, 3, 4, 5]

list2 = copy.deepcopy(list1)
print(list1)
print(list2)
print(id(list1))
print(id(list2))


list3 = copy.copy(list1)
print(list1)
print(list3)
print(id(list1))
print(id(list3))


list1.append(6)
print(list1)
print(list2)
print(list3)
print(id(list1))
print(id(list2))
print(id(list3))

print("*********************Shallow copy only shares nested mutable objects, not the outer list.***************************")

list4 = [[1, 2], [3, 4]]
list5 = copy.copy(list4)

list4[0].append(99)

print(list4)  # [[1, 2, 99], [3, 4]]
print(list5)  # [[1, 2, 99], [3, 4]] 