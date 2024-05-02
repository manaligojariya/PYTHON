# Write a Python program to combine two dictionary adding values for 
# common keys.
# o d1 = {'a': 100, 'b': 200, 'c':300}
# o d2 = {'a': 300, 'b': 200,’d’:400}

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict={}

for key in d1:
    if key in d2:
        combined_dict[key]=d1[key]+d2[key]
    else:
        combined_dict[key]=d1[key]

for key in d2:
    if key not in d1:
        combined_dict[key]=d2[key]

print(combined_dict)
        
