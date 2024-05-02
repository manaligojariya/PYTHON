# Write a Python program to check multiple keys exists in a dictionary

mydict={'apple':3, 'banana':2, 'cherry':5, 'date':4, 'fig':1}

keys_to_check=['apple','banana','grape']

for key in keys_to_check:
    if key in mydict:
        print(f"'{key}' exists in the dictionary.")
    else:
        print(f"'{key}' does not exists in the dictionary.")