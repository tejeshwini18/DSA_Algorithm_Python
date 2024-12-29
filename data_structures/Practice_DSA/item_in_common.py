def item_in_common(list1,list2):
    all_item = {}
    for i in list1:
        all_item[i] = True
    for j in list2:
        if j in all_item:
            return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""