def find_max_min(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[j]<my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i],my_list[min_index] = my_list[min_index],my_list[i]
    return my_list[-1],my_list[0]
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""