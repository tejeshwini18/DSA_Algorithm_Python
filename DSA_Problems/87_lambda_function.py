input_list = [1,2,3,4,5]

mapped_list = list(map(lambda x: x*2, input_list))
print("mapped_list: ",mapped_list)


filtered_list = list(filter(lambda x: x%2==0, input_list))
print("filtered_list: ",filtered_list)

from functools import reduce
reduced_list = reduce(lambda x,y: x+y, input_list)
print("reduced_list: ",reduced_list)


squared_list = list(map(lambda x: x**2, input_list))
print("squared_list: ",squared_list)


cubed_list = list(map(lambda x: x**3, input_list))
print("cubed_list: ",cubed_list)

even_list = list(filter(lambda x: x%2==0, input_list))
print("even_list: ",even_list)

odd_list = list(filter(lambda x: x%2!=0, input_list))
print("odd_list: ",odd_list)