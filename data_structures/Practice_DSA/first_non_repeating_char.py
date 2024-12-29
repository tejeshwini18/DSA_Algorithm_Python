def first_non_repeating_char(str1):
    str_dict = {}
    # Count occurrences of each character
    for ch in str1:
        if ch in str_dict:
            str_dict[ch] += 1
        else:
            str_dict[ch] = 1
            
    # Find the first character with count 1
    for ch in str1:
        if str_dict[ch] == 1:
            return ch
    
    return None


print(first_non_repeating_char('leetcode'))  # Expected output: l
print(first_non_repeating_char('hello'))     # Expected output: h
print(first_non_repeating_char('aabbcc'))    # Expected output: None
