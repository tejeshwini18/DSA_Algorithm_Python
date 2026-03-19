
def flatten_dict(d, parent_key='', sep = '.'):
    result = {}
    for key, val in d.items():
        new_key = parent_key + sep + key if parent_key else key

        if isinstance(val,dict):
            result.update(flatten_dict(val,new_key,sep))
        else:
            result[new_key]=val
    return result


input1 = {"a":1,"b":{"c":2}}
input2 = {"x":{"y":{"z":5}}}
input3 = {"a":1,"b":{"c":2,"d":3}}
input4 = {"a":{"b":{"c":{"d":4}}}}
input5 = {"user":{"name":"Tej","addr":{"city":"Pune"}}}
input6 = {"k1":1,"k2":{"k3":{"k4":2}}}
input7 = {"a":{},"b":2}
input8 = {"a":{"b":1},"c":{"d":2,"e":{"f":3}}}

output1 = flatten_dict(input1)
output2 = flatten_dict(input2)
output3 = flatten_dict(input3)
output4 = flatten_dict(input4)
output5 = flatten_dict(input5)
output6 = flatten_dict(input6)
output7 = flatten_dict(input7)
output8 = flatten_dict(input8)

print(output1)
print("******************************")
print(output2)
print("******************************")
print(output3)
print("******************************")
print(output4)
print("******************************")
print(output5)
print("******************************")
print(output6)
print("******************************")
print(output7)
print("******************************")
print(output8)
print("******************************")