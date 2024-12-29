def group_anagrams(str_list):
    anagram_dict = {}
    
    for word in str_list:
        # Sort the word to create a key
        key = ''.join(sorted(word))
        # Group words with the same key
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]
    
    # Return the grouped anagrams as a list of lists
    return list(anagram_dict.values())


# Test cases
print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))
