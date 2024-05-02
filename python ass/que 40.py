# Write a Python program to map two lists into a dictionary

keys=['a','b','c']
value=[1,2,3]

result_dict={}

for i in range(len(keys)):
    result_dict[keys[i]]=value[i]

print(result_dict)

