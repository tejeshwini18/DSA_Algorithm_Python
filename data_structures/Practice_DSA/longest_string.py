def find_longest_string(my_list):
    if not my_list:
        return ''
    len_dict = {}
    for val in my_list:
        len_dict[val] = len(val)
    max_str = max(len_dict,key=len_dict.get)
    return max_str


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""