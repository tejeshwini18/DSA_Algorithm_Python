from collections import defaultdict

def group_anagram(in_list):
    groups = defaultdict(list)

    for word in in_list:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

out_list=group_anagram(['eat','egg','you','ate','tea'])
print(out_list)